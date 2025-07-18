from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

# python -m uvicorn app.main:app --reload
