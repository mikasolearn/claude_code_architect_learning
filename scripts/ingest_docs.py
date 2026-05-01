import chromadb
from chromadb.utils import embedding_functions
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os, glob

client = chromadb.PersistentClient(path="./vectordb")
embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

def ingest_collection(name, file_paths, chunk_size=800, overlap=100):
    coll = client.get_or_create_collection(name=name, embedding_function=embedder)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=overlap
    )
    docs, ids, metas = [], [], []
    for path in file_paths:
        if path.endswith(".pdf"):
            text = "\n".join(p.extract_text() or "" for p in PdfReader(path).pages)
        else:
            text = open(path, encoding="utf-8").read()
        for i, chunk in enumerate(splitter.split_text(text)):
            docs.append(chunk)
            ids.append(f"{os.path.basename(path)}-{i}")
            metas.append({"source": path})
    coll.upsert(documents=docs, ids=ids, metadatas=metas)
    print(f"Ingested {len(docs)} chunks into '{name}'")

ingest_collection("exam_format", glob.glob("knowledge/exam-blueprint/*.pdf"))
ingest_collection("cc_docs", glob.glob("knowledge/claude-code-docs/**/*.md", recursive=True))