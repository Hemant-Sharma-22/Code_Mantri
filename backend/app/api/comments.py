from fastapi import APIRouter

from app.schemas.analyze_schema import AnalyzeRequest
from app.ai.gemini_service import generate_comments

router = APIRouter()


@router.post("/comments")
def comments(request: AnalyzeRequest):

    analysis = generate_comments(

        code=request.code,

        language=request.language,

        title=request.title,

        url=request.url,

        page_context=request.page_context,

        platform=request.platform

    )

    return {

        "title": "Code Comments",

        "analysis": analysis

    }