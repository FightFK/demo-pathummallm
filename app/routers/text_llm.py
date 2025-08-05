from fastapi import APIRouter
from pydantic import BaseModel
from services.pathumma import generate_text
from typing import Optional

router = APIRouter()

class TextGenerateRequest(BaseModel):
    instruction: str
    system_prompt: Optional[str] = None
    max_new_tokens: int = 512
    temperature: float = 0.4
    return_json: bool = True

@router.post("/generate")
async def text_generate(request: TextGenerateRequest):
    return await generate_text(
        instruction=request.instruction,
        system_prompt=request.system_prompt,
        max_new_tokens=request.max_new_tokens,
        temperature=request.temperature,
        return_json=request.return_json
    )
