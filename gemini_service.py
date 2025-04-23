import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=GEMINI_API_KEY)

def analyze_health_status(user_input):
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(user_input)
    return response.text

if __name__ == "__main__":
    user_input = "ile jest 2 + 2?"
    print(analyze_health_status(user_input))
