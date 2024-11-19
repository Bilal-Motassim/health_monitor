# utils.py

import os
import requests

LLAMA_ENDPOINT = os.getenv("LLAMA_ENDPOINT", "http://localhost:11434/v1/chat/completions")

def send_prompt_to_llm(prompt, model="llama3"):
    response = requests.post(
        LLAMA_ENDPOINT,
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    response.raise_for_status()  
    return response.json()["choices"][0]["message"]["content"]
