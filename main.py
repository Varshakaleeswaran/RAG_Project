import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.create_collection(name="ai_knowledge")
with open("data/ai_dataset.txt", "r", encoding="utf-8") as f:
    text = f.read()
chunks = text.split("\n\n")
embeddings = model.encode(chunks).tolist()
collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(chunks))]
)

print("Dataset stored in ChromaDB!")

while True:
    query = input("\nAsk a question (type 'exit' to stop): ")
    
    if query.lower() == "exit":
        break

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=2
    )

    print("\n🔍 Retrieved Context:")
    for doc in results["documents"][0]:
        print("-", doc)

    print("\n Answer:")
    print(results["documents"][0][0])