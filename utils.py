def normalize(model, text):
    return {
        "model": model,
        "response": text,
        "length": len(text)
    }
