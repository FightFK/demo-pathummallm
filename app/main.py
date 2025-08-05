from fastapi import FastAPI
from routers import text_llm, audio_llm, vision_llm

app = FastAPI(title="Pathumma LLM API")

app.include_router(text_llm.router, prefix="/text", tags=["Text LLM"])
app.include_router(audio_llm.router, prefix="/audio", tags=["Audio LLM"])
app.include_router(vision_llm.router, prefix="/vision", tags=["Vision LLM"])

@app.get("/")
def root():
  return {"message": "Pathumma LLM API is running."}
