import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:8000",
    "X-Title": "UniQuery AI"
}

async def call_model(model_id: str, query: str):
    async with httpx.AsyncClient(timeout=60) as client:
        res = await client.post(
            BASE_URL,
            headers=HEADERS,
            json={
                "model": model_id,
                "messages": [
                    {"role": "user", "content": query}
                ]
            }
        )

    if res.status_code != 200:
        return f"ERROR [{model_id}]: {res.text}"

    data = res.json()
    return data["choices"][0]["message"]["content"]


# Mistral AI
async def mistral_response(query: str):
    return await call_model(
        "mistralai/mistral-7b-instruct:free",
        query
    )


#  Gemini-style (Gemma)
async def gemini_response(query: str):
    return await call_model(
        "google/gemma-3-27b-it:free",
        query
    )

#  DeepSeek
async def deepseek_response(query: str):
    return await call_model(
        "tngtech/deepseek-r1t2-chimera:free",
        query
    )
