import streamlit as st
from google import genai
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Configuration
MY_API_KEY = "your_api_key_here"
client = genai.Client(api_key=MY_API_KEY)

# Page Configuration
st.set_page_config(page_title="AI Teaching Assistant", page_icon="🎓")
st.title("🎓 AI Teaching Assistant")
st.markdown("Ask me anything about your course materials!")

# Database Connection
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", 
    google_api_key=MY_API_KEY
)
vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

# Chat Interface
if query := st.chat_input("Type your question here..."):
    with st.chat_message("user"):
        st.markdown(query)
    
    # RAG Retrieval
    with st.spinner("Searching for answers..."):
        docs = vector_db.similarity_search(query, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        prompt = f"Based on the following context, provide a helpful and professional answer:\n{context}\n\nQuestion: {query}"
        
        # Generation
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
    
    # Display response
    with st.chat_message("assistant"):
        st.markdown(response.text)