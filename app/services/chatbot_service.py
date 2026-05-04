import requests
from app.config import GEMINI_API_KEY

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

def get_chatbot_response(question: str):
    data = {
        "contents": [
            {"parts": [{"text": question}]}
        ]
    }

    res = requests.post(URL, json=data)
    result = res.json()
    
    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Error: No response"
