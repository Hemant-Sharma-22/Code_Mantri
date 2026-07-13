from fastapi import FastAPI
from app.api.analyze import router as analyze_router
from app.api.bugs import router as bugs_router
from app.api.optimize import router as optimize_router
from app.api.comments import router as comments_router
from app.api.translate import router as translate_router
from app.api.complexity import router as complexity_router
from app.api.tests import router as tests_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.generate import router as generate_router

app = FastAPI(
    title="AI Code Mentor API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router)
app.include_router(bugs_router)
app.include_router(optimize_router)
app.include_router(comments_router)
app.include_router(translate_router)
app.include_router(complexity_router)
app.include_router(tests_router)
app.include_router(generate_router)

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