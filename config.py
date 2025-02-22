import os

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "Failed to get secret key")
