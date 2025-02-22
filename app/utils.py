import os
from google import genai

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(prompt):
    """Send a prompt to Google Gemini and return the response."""
    try:
        response = client.models.generate_content(
            model="gemini-pro", contents=prompt)
        return response.text if response else "No response from Gemini"
    except Exception as e:
        return f"Error: {str(e)}"
