import os
from aift.multimodal import textqa
from dotenv import load_dotenv

load_dotenv()

from aift import setting

setting.set_api_key(os.getenv("AIFT_API_KEY"))

async def generate_text(instruction, system_prompt, max_new_tokens, temperature, return_json):
    result = textqa.generate(
        instruction=instruction,
        system_prompt=system_prompt,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        return_json=return_json,
    )
    # recive from postman as a json
    if return_json:
        return result.get("content")
    else:
        return result
