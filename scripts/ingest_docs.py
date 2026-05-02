import chromadb
from chromadb.utils import embedding_functions
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownTextSplitter
import os, glob, json, hashlib, time
from pathlib import Path
from tqdm import tqdm

# ---------- Setup ----------
CHECKPOINT_DIR = Path("./checkpoints")
CHECKPOINT_DIR.mkdir(exist_ok=True)

client = chromadb.PersistentClient(path="./vectordb")
embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# ---------- Checkpoint helpers ----------
def checkpoint_path(collection_name):
    return CHECKPOINT_DIR / f"{collection_name}.json"

def load_checkpoint(collection_name):
    p = checkpoint_path(collection_name)
    if p.exists():
        with open(p) as f:
            return json.load(f)
    return {"completed_files": {}, "failed_files": {}}

def save_checkpoint(collection_name, state):
    p = checkpoint_path(collection_name)
    tmp = p.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(state, f, indent=2)
    tmp.replace(p)  # atomic write

def file_hash(path):
    """Hash the file so re-ingestion happens if file changed."""
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

# ---------- Text extraction ----------
def extract_text(path):
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        return "\n".join(p.extract_text() or "" for p in reader.pages)
    else:
        with open(path, encoding="utf-8") as f:
            return f.read()

# ---------- Smart splitter selection ----------
def get_splitter(file_path, chunk_size, overlap):
    """
    Choose splitter based on file type.
    - Markdown gets a markdown-aware splitter (preserves headings/sections).
    - PDFs/text use Recursive splitter with semantic separators.
    """
    if file_path.endswith(".md"):
        return MarkdownTextSplitter(
            chunk_size=chunk_size, chunk_overlap=overlap
        )
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

# ---------- Ingestion ----------
def ingest_collection(
    name,
    file_paths,
    chunk_size=512,        # ~tokens-friendly for MiniLM (max 256 tokens ≈ 1000 chars)
    overlap=80,            # ~15% overlap, good context preservation
    batch_size=64,         # batch upserts to chroma
    force_reingest=False,
):
    if not file_paths:
        print(f"⚠️  No files for '{name}'")
        return

    coll = client.get_or_create_collection(name=name, embedding_function=embedder)
    state = load_checkpoint(name)

    print(f"\n=== Ingesting collection: '{name}' ({len(file_paths)} files) ===")

    for path in tqdm(file_paths, desc=f"[{name}] files"):
        try:
            fhash = file_hash(path)

            # Skip if already done & unchanged
            prev = state["completed_files"].get(path)
            if not force_reingest and prev and prev.get("hash") == fhash:
                continue

            # If re-ingesting, delete old chunks for this file first
            if prev:
                try:
                    coll.delete(where={"source": path})
                except Exception:
                    pass

            text = extract_text(path)
            if not text.strip():
                state["failed_files"][path] = "empty text"
                save_checkpoint(name, state)
                continue

            splitter = get_splitter(path, chunk_size, overlap)
            chunks = splitter.split_text(text)

            # Batched upsert (helps avoid memory spikes / partial fails)
            base = os.path.basename(path)
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i + batch_size]
                ids = [f"{base}-{fhash[:8]}-{i + j}" for j in range(len(batch))]
                metas = [{"source": path, "chunk_index": i + j} for j in range(len(batch))]
                coll.upsert(documents=batch, ids=ids, metadatas=metas)

            # Mark file complete + checkpoint
            state["completed_files"][path] = {
                "hash": fhash,
                "chunks": len(chunks),
                "ts": time.time(),
            }
            state["failed_files"].pop(path, None)
            save_checkpoint(name, state)

        except Exception as e:
            print(f"❌ Failed '{path}': {e}")
            state["failed_files"][path] = str(e)
            save_checkpoint(name, state)
            continue

    total_chunks = sum(v["chunks"] for v in state["completed_files"].values())
    print(f"✅ '{name}': {len(state['completed_files'])} files, {total_chunks} total chunks")
    if state["failed_files"]:
        print(f"⚠️  {len(state['failed_files'])} failed files: {list(state['failed_files'])}")


# ---------- Run ----------
if __name__ == "__main__":
    ingest_collection(
        "exam_format",
        glob.glob("knowledge/exam-blueprint/*.pdf"),
        chunk_size=600,   # PDFs/exam blueprints: smaller for precise retrieval
        overlap=100,
    )
    ingest_collection(
        "cc_docs",
        glob.glob("knowledge/claude-code-docs/**/*.md", recursive=True),
        chunk_size=800,   # docs: larger for more context per chunk
        overlap=120,
    )