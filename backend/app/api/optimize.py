from fastapi import APIRouter

from app.schemas.analyze_schema import AnalyzeRequest
from app.ai.gemini_service import optimize_code

router = APIRouter()


@router.post("/optimize")
def optimize(request: AnalyzeRequest):

    analysis = optimize_code(

        code=request.code,

        language=request.language,

        title=request.title,

        url=request.url,

        page_context=request.page_context,

        platform=request.platform

    )

    return {

        "title": "Code Optimization",

        "analysis": analysis

    }