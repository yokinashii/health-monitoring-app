import google.generativeai as genai
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

@app.get("/analyze")
def analyze(query: str):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(query)
        print("ODPOWIEDŹ GEMINI:", response.text)
        return {"response": response.text or "Brak odpowiedzi z AI"}
    except Exception as e:
        print("BŁĄD W AI SERVICE:", e)
        return {"response": f"Błąd: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
