import os
from aift.multimodal import vqa
from dotenv import load_dotenv

load_dotenv()

from aift import setting

setting.set_api_key(os.getenv("AIFT_API_KEY"))

def vision(file_path, instruction):
  result = vqa.generate(
      file_path=file_path,
      instruction=instruction
  )

  return result.get("content") if result else None