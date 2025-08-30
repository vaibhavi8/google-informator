from fastapi import APIRouter, Request
from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

router = APIRouter()

@router.post("/vector_stores/add_file")
async def add_file(request: Request):
    data = await request.json()
    vector_store_id = data.get("vectorStoreId")
    file_id = data.get("fileId")
    try:
        response = openai.VectorStoreFile.create(
            vector_store_id=vector_store_id,
            file_id=file_id
        )
        return {"vectorStore": response}
    except Exception as e:
        print("Error adding file:", e)
        return {"error": "Error adding file"}

@router.post("/vector_stores/create_store")
async def create_store(request: Request):
    data = await request.json()
    name = data.get("name")
    try:
        response = openai.VectorStore.create(name=name)
        return {"vectorStore": response}
    except Exception as e:
        print("Error creating vector store:", e)
        return {"error": "Error creating vector store"}

@router.get("/vector_stores/list_files")
async def list_files(vector_store_id: str):
    try:
        response = openai.VectorStoreFile.list(vector_store_id=vector_store_id)
        return {"files": response}
    except Exception as e:
        print("Error fetching files:", e)
        return {"error": "Error fetching files"}

@router.get("/vector_stores/retrieve_store")
async def retrieve_store(vector_store_id: str):
    try:
        response = openai.VectorStore.retrieve(vector_store_id=vector_store_id)
        return {"vectorStore": response}
    except Exception as e:
        print("Error fetching vector store:", e)
        return {"error": "Error fetching vector store"}

@router.post("/vector_stores/upload_file")
async def upload_file(request: Request):
    data = await request.json()
    file_object = data.get("fileObject")
    try:
        file_buffer = bytes(file_object["content"], "utf-8")
        response = client.files.create(file=file_buffer,
        purpose="assistants")
        return {"file": response}
    except Exception as e:
        print("Error uploading file:", e)
        return {"error": "Error uploading file"}
