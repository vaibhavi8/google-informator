from fastapi import APIRouter, Request

import requests
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()


openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


import json

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    injectable_prompt = "You are a helpful assistant."
    prompt = data.get("prompt")
    final_prompt = injectable_prompt + prompt
    print("Prompt sent to OpenAI:", prompt)  # Debug log

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": final_prompt}]
    )
    reply = response.choices[0].message.content
    return {"reply": reply}