from fastapi import APIRouter, Request
from openai import OpenAI
import os


from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

client = OpenAI()  # Uses OPENAI_API_KEY from environment

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}])
    return {"reply": response.choices[0].message.content}
