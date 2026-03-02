import chromadb
from sentence_transformers import SentenceTransformer

# ----------------------------
# Load embedding model
# ----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# ----------------------------
# Initialize ChromaDB
# ----------------------------
client = chromadb.Client()
collection = client.create_collection(name="ai_knowledge")

# ----------------------------
# Load dataset
# ----------------------------
with open("data/ai_dataset.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ----------------------------
# Split into chunks
# ----------------------------
chunks = text.split("\n\n")

# ----------------------------
# Create embeddings
# ----------------------------
embeddings = model.encode(chunks).tolist()

# ----------------------------
# Store in ChromaDB
# ----------------------------
collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(chunks))]
)

print("✅ Dataset stored in ChromaDB!")

# ----------------------------
# Query loop
# ----------------------------
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

    print("\n🤖 Answer:")
    print(results["documents"][0][0])