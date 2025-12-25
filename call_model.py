mistral_ans = await call_model(
    "mistralai/mistral-7b-instruct:free",
    query
)


gemini_ans = await call_model(
    "google/gemma-3-27b-it:free",
    query
)

deepseek_ans = await call_model(
    "tngtech/deepseek-r1t2-chimera:free",
    query
)
