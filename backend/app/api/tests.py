from fastapi import APIRouter

from app.schemas.analyze_schema import AnalyzeRequest
from app.ai.gemini_service import generate_tests

router = APIRouter()


@router.post("/tests")
def tests(request: AnalyzeRequest):

    analysis = generate_tests(

        code=request.code,

        language=request.language,

        title=request.title,

        url=request.url,

        page_context=request.page_context,

        platform=request.platform

    )

    return {

        "title": "Unit Test Generation",

        "analysis": analysis

    }