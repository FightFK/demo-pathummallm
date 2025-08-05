import os
from aift.multimodal import audioqa
from dotenv import load_dotenv

load_dotenv()

from aift import setting

setting.set_api_key(os.getenv("AIFT_API_KEY"))

def generate_audio(file_path, instruction):
  """
  Generate audio transcription or processing based on the provided file and instruction.
  
  :param file_path: Path to the audio file.
  :param instruction: Instruction for processing the audio.
  :return: Processed audio result.
  """
  result = audioqa.generate(
      file_path=file_path,
      instruction=instruction
  )
  
  return result.get("content") if result else None
