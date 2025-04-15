from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import players

app = FastAPI(title="FSU Football Player API")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:8080"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(players.router, prefix="/api")