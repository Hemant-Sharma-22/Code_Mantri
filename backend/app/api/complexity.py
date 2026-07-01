from fastapi import APIRouter

from app.schemas.analyze_schema import AnalyzeRequest
from app.ai.gemini_service import analyze_complexity

router = APIRouter()


@router.post("/complexity")
def complexity(request: AnalyzeRequest):

    analysis = analyze_complexity(

        code=request.code,

        language=request.language,

        title=request.title,

        url=request.url,

        page_context=request.page_context,

        platform=request.platform

    )

    return {

        "title": "Complexity Analysis",

        "analysis": analysis

    }