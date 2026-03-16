import os
from google import genai
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# 사용할 API 키를 변수에 저장
MY_API_KEY = "your_api_key_here"

# 1. API 클라이언트 설정
client = genai.Client(api_key=MY_API_KEY)

# 2. 임베딩 연결 (여기에도 google_api_key를 넣어줘야 합니다!)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", 
    google_api_key=MY_API_KEY
)
vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

# 3. 질문 및 검색
query = input("Ask your AI TA a question: ")
docs = vector_db.similarity_search(query, k=3)
context = "\n".join([doc.page_content for doc in docs])

# 4. 답변 생성
prompt = f"다음 문맥을 바탕으로 질문에 답변하세요:\n{context}\n\n질문: {query}"
response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents=prompt
)

print("\n--- AI TA Answer ---")
print(response.text)