import os
from google import genai

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(message):
    """Send a prompt to Google Gemini and return the response."""
    try:
        prompt = f"""You are a recruiter evaluating a candidate’s speech. Provide feedback on the speech, the sentiments expressed, and the overall impact. Finally, give the candidate a score out of 10. Be brutally honest with the rating.
        {message}
        
        
        Start and end your response with a # to indicate the beginning and end of your feedback.
    """
        response = client.models.generate_content(
            model="gemini-pro", contents=prompt)
        
        return response.json() if response else "No response from Gemini"
    except Exception as e:
        return f"Error: {str(e)}"
