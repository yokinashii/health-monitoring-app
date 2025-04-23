from fastapi import FastAPI

app = FastAPI()

health_data = {
    1: {"steps": 10000, "calories": 500},
    2: {"steps": 7500, "calories": 400}
}

@app.get("/health/{user_id}")
def get_health(user_id: int):
    return health_data.get(user_id, {"error": "Health data not found"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
