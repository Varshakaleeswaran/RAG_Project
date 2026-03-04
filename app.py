import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from pdf_utils import extract_text_from_pdf

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
client = chromadb.Client()
collection = client.get_or_create_collection("pdf_collection")

st.title(" AI PDF Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    chunks = text.split("\n\n")
    embeddings = model.encode(chunks).tolist()

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[str(i) for i in range(len(chunks))]
    )

    st.success("PDF processed successfully!")

    query = st.text_input("Ask a question from the PDF")

    if query:
        query_embedding = model.encode([query]).tolist()

        results = collection.query(
            query_embeddings=query_embedding,
            n_results=2
        )

        st.subheader("Answer:")
        st.write(results["documents"][0][0])