from fastapi import FastAPI
from llm_connectors import (
    mistral_response,
    gemini_response,
    deepseek_response
)
from utils import normalize

app = FastAPI(title="UniQuery AI")

@app.post("/ask")
async def ask(query: str):

    mistral_ans = await mistral_response(query)
    gemini_ans = await gemini_response(query)
    deepseek_ans = await deepseek_response(query)

    results = []

    for model, ans in [
        ("Mistral AI (Mistral 7B)", mistral_ans),
        ("Gemini (Gemma-3-27B)", gemini_ans),
        ("DeepSeek R1T2 Chimera", deepseek_ans)
    ]:
        if ans and not ans.startswith("ERROR"):
            results.append(normalize(model, ans))

    return {
        "query": query,
        "results": results
    }
