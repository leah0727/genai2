from mcp.server.fastmcp import FastMCP
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

# 1. API 키 설정 (보안상 환경변수 권장)
os.environ["GOOGLE_API_KEY"] = "your_api_key_here"

# 2. MCP 서버 이름 정의
mcp = FastMCP("Course-Assistant-MCP")

# 3. 벡터 DB 연결 (기존 경로 그대로 사용)
embeddings = GoogleGenerativeAIEmbeddings(model="embedding-001")
vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

# 4. MCP 도구 정의: AI가 이 함수를 호출해서 정보를 가져감
@mcp.tool()
def search_course_notes(query: str) -> str:
    """사용자의 질문에 대해 강의 노트를 검색하여 관련 내용을 반환합니다."""
    docs = vector_db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])

if __name__ == "__main__":
    mcp.run()