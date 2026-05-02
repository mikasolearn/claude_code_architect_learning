import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="./vectordb")
embedder = embedding_functions.DefaultEmbeddingFunction()  
coll = client.get_collection("cc_docs", embedding_function=embedder)

results = coll.query(query_texts=["how do I use subagents?"], n_results=3)

for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
    print(f"\n[distance={dist:.3f}] {meta['source']}")
    print(doc[:300])