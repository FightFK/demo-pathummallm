from dotenv import load_dotenv
import os

load_dotenv()  # โหลด .env

PATHUMMA_API_KEY = os.getenv("PATHUMMA_API_KEY")
PATHUMMA_API_URL = os.getenv("PATHUMMA_API_URL", "https://api.pathumma.example/v1/llm")
