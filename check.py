import os
import google.generativeai as genai

# 직접 키를 입력하세요 (테스트용)
api_key = "your_api_key_here"


try:
    genai.configure(api_key=api_key)
    print("API Configuration successful!")
    
    models = genai.list_models()
    found = False
    for m in models:
        if 'embed' in m.name:
            print(f"Found model: {m.name}")
            found = True
            
    if not found:
        print("No embedding models found.")
        
except Exception as e:
    print(f"An error occurred: {e}")