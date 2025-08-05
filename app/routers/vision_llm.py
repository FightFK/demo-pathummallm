from fastapi import APIRouter, UploadFile
from services.vision_qa import vision

router = APIRouter()

@router.post("/vision")
async def vision_process(file: UploadFile, instruction: str):
    contents = await file.read()
    result = await vision(contents, instruction)
    return { "result": result }
