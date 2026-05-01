import sys, chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="./vectordb")
embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
collection = client.get_collection(sys.argv[1], embedding_function=embedder)
query = sys.argv[2]
k = int(sys.argv[sys.argv.index("--k")+1]) if "--k" in sys.argv else 5

results = collection.query(query_texts=[query], n_results=k)
for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
    print(f"--- {meta['source']} ---\n{doc}\n")