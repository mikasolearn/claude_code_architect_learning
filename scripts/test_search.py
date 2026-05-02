from pathlib import Path
import chromadb, glob, os, json, hashlib, time
from chromadb.utils import embedding_functions
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownTextSplitter
from tqdm import tqdm

# ---------- Paths ----------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
VECTORDB_PATH = PROJECT_ROOT / "vectordb"
CHECKPOINT_DIR = PROJECT_ROOT / "checkpoints"
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"

CHECKPOINT_DIR.mkdir(exist_ok=True)

client = chromadb.PersistentClient(path=str(VECTORDB_PATH))
embedder = embedding_functions.DefaultEmbeddingFunction()  
coll = client.get_collection("cc_docs", embedding_function=embedder)

results = coll.query(query_texts=["how do I use subagents?"], n_results=3)

for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
    print(f"\n[distance={dist:.3f}] {meta['source']}")
    print(doc[:300])