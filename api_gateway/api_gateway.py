from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lub konkretny frontend jak: ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


USERS_SERVICE_URL = "http://users_service:8001"
HEALTH_SERVICE_URL = "http://health_service:8002"
AI_SERVICE_URL = "http://ai_service:8003"

@app.get("/")
def root():
    return {"message": "API Gateway działa!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    response = requests.get(f"{USERS_SERVICE_URL}/users/{user_id}")
    return response.json()

@app.get("/health/{user_id}")
def get_health(user_id: int):
    response = requests.get(f"{HEALTH_SERVICE_URL}/health/{user_id}")
    return response.json()

@app.get("/ai/analyze")
def analyze(query: str):
    response = requests.get(f"{AI_SERVICE_URL}/analyze?query={query}")
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
