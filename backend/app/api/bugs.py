from fastapi import APIRouter

from app.schemas.analyze_schema import AnalyzeRequest
from app.ai.gemini_service import detect_bugs

router = APIRouter()


@router.post("/bugs")
def bugs(request: AnalyzeRequest):

    analysis = detect_bugs(

        code=request.code,

        language=request.language,

        title=request.title,

        url=request.url,

        page_context=request.page_context,

        platform=request.platform

    )

    return {

        "title": "Bug Detection",

        "analysis": analysis

    }