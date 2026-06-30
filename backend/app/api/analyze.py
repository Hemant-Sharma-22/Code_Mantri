from fastapi import APIRouter

from app.schemas.analyze_schema import AnalyzeRequest
from app.ai.gemini_service import explain_code

router = APIRouter()


@router.post("/analyze")
def analyze(request: AnalyzeRequest):

    analysis = explain_code(
    code=request.code,
    language=request.language
)

    return {
        "title": "AI Analysis",
        "analysis": analysis
    }