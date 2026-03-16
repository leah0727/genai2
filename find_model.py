from google import genai

# API 키 설정
client = genai.Client(api_key="your_api_key_here")

# 사용 가능한 모델 목록 가져오기
models = client.models.list()
for model in models:
    print(f"모델 이름: {model.name}, 지원 기능: {model.supported_generation_methods}")
    