# 🧠 Health Monitoring App

**Health Monitoring App** to mikroserwisowa aplikacja webowa służąca do analizy zdrowia użytkownika i generowania rekomendacji AI. System umożliwia zadawanie pytań dotyczących zdrowia i kondycji fizycznej oraz przechowuje dane użytkowników i ich parametrów zdrowotnych.

## 🔧 Technologie

- **Python + FastAPI** (każdy mikroserwis)
- **Docker** (konteneryzacja)
- **Docker Compose** (zarządzanie całością)
- **Google Gemini AI (genai)** – generowanie odpowiedzi AI
- **Swagger/OpenAPI** – dokumentacja API
- **JWT** – uwierzytelnianie użytkowników
- **Pytest** – testy jednostkowe i integracyjne
- **Auto-scaler** (Docker SDK) – automatyczne skalowanie mikroserwisu AI

## 🧩 Mikroserwisy

- `api_gateway` – punkt wejścia, łączy wszystkie serwisy
- `ai_service` – integracja z Google Gemini API
- `users_service` – dane użytkowników i logowanie (JWT)
- `health_service` – parametry zdrowotne (wiek, wzrost, waga, itd.)

## ⚙️ Uruchomienie projektu lokalnie

1. **Sklonuj repozytorium**:
   ```bash
   git clone https://github.com/yokinashii/health-monitoring-app.git
   cd health-monitoring-app

1. **Utwórz plik .env**:
   ```bash
   GEMINI_API_KEY=tu_wklej_swoj_klucz
   
3. **Uruchom aplikację**:
   ```bash
   docker compose up --build
   
4. **Wejdź do dokumentacji API:**:
   http://localhost:8000/docs

### Członkowie zespołu
- **Adrian Adamus** (Lider)
- Repozytorium: https://github.com/yokinashii/health-monitoring-app