import google.generativeai as genai
import os
from dotenv import load_dotenv

# Załaduj klucz API
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Konfiguracja klienta
genai.configure(api_key=GEMINI_API_KEY)

# Pobierz dostępne modele
models = genai.list_models()
for model in models:
    print(model.name)
