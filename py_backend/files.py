from fastapi import APIRouter, Request
import requests
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.get("/container_files/content")
async def get_container_file(file_id: str, container_id: str = None, filename: str = None):
    if container_id:
        url = f"https://api.openai.com/v1/containers/{container_id}/files/{file_id}/content"
    else:
        url = f"https://api.openai.com/v1/container-files/{file_id}/content"
    headers = {"Authorization": f"Bearer YOUR_OPENAI_API_KEY"}
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code != 200:
        return {"error": "Failed to fetch file"}
    return StreamingResponse(response.raw, media_type=response.headers.get("Content-Type", "application/octet-stream"),
                             headers={"Content-Disposition": f"attachment; filename={filename or file_id}"})
