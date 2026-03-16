import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# 1. Setup API Key (Make sure to set this in your terminal or replace the string)
os.environ["GOOGLE_API_KEY"] = "your_api_key_here"

# 2. Data Ingestion: Load and Split
print("Loading and splitting documents...")
loader = DirectoryLoader('./data', glob="./*.pdf", loader_cls=PyPDFLoader)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)
print(f"Processed {len(chunks)} chunks.")

# 3. Embedding and Storage
print("Embedding and storing in ChromaDB...")
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# This creates the vector store
vector_db = Chroma.from_documents(
    documents=chunks, 
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("Knowledge base built successfully!")