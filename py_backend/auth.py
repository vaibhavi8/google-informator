from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from authlib.integrations.starlette_client import OAuth
import os

oauth = OAuth()
oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://oauth2.googleapis.com/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile https://www.googleapis.com/auth/calendar'}
)

router = APIRouter()

@router.get("/google/auth")
async def google_auth(request: Request):
    redirect_uri = "http://localhost:8000/google/callback"
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/google/callback")
async def google_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)
    return JSONResponse({"token": token, "user": user})

@router.get("/google/status")
async def google_status():
    return JSONResponse({"connected": False, "oauthConfigured": True})
