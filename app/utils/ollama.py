import requests

def generate_from_ollama(prompt: str):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        return res.json()["response"]

    except Exception as e:
        return f"Error: {str(e)}"