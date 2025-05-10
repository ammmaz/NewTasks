from fastapi import FastAPI, Request
from evaluator import evaluate_flags
import uvicorn

app = FastAPI()

@app.get("/flags")
def get_flags(user: str, region: str):
    return evaluate_flags(user, region)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=9000)
