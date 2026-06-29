from fastapi import FastAPI
from app.api.analyze import router as analyze_router

app = FastAPI(
    title="AI Code Mentor API",
    version="1.0.0"
)

app.include_router(analyze_router)


@app.get("/")
def home():
    return {
        "message": "AI Code Mentor Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }