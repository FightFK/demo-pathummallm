from fastapi import APIRouter, UploadFile
from services.audio_qa import generate_audio

router = APIRouter()

@router.post("/audio")
async def audio_process(file: UploadFile, instruction: str):
    contents = await file.read()
    result = await generate_audio(contents, instruction)
    return { "result": result}
