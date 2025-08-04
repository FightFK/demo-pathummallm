from fastapi import FastAPI
from app.routers import text_llm

app = FastAPI(title="Pathumma LLM API")

app.include_router(text_llm.router, prefix="/text", tags=["Text LLM"])


@app.get("/")
async def root():
    return {"message": "Pathumma LLM API is running."}
