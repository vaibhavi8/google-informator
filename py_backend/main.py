from fastapi import FastAPI
from auth import router as auth_router
from vector_store import router as vector_store_router
from files import router as files_router
from utils import router as utils_router
from chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware



app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="asdfAfJNKF023Fdfn")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(vector_store_router)
app.include_router(files_router)
app.include_router(utils_router)
app.include_router(chat_router)

@app.get("/")
async def root():
    return {"status": "ok"}
