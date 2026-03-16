from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
import os

# 1. Set up the embedding model (Gemini's embedding)
# Ensure you have set your GOOGLE_API_KEY environment variable
os.environ["GOOGLE_API_KEY"] = "your_api_key_here"

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 2. Store chunks in ChromaDB
# This converts text into vectors and saves them locally
vector_db = Chroma.from_documents(
    documents=chunks, 
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("Embedding complete! Data has been stored in './chroma_db'.")