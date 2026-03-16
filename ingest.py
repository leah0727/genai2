import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load PDFs from the 'data' directory
# Ensure your PDF files are located in the './data' folder
loader = DirectoryLoader('./data', glob="./*.pdf", loader_cls=PyPDFLoader)
documents = loader.load()

# 2. Split documents into smaller, manageable chunks
# chunk_size: number of characters per chunk
# chunk_overlap: overlapping characters to maintain context between chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Successfully split {len(documents)} document(s) into {len(chunks)} chunks.")
print(f"Sample chunk: {chunks[0].page_content[:100]}...")