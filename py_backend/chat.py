from fastapi import APIRouter, Request

import requests

router = APIRouter()



import json

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    print("Prompt sent to Ollama:", prompt)  # Debug log

    ollama_response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt
        },
        stream=True
    )

    response_text = ""
    for line in ollama_response.iter_lines():
        if line:
            obj = json.loads(line.decode("utf-8"))
            # print("Ollama chunk:", obj)  # Debug log
            response_text += obj.get("response", "")

            # If model is still loading, return a message
            if obj.get("done_reason") == "load":
                return {"reply": "Model is loading, please try again in a few seconds."}

    return {"reply": response_text}