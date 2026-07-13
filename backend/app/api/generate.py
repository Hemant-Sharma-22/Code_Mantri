from fastapi import APIRouter

from app.schemas.generate_schema import GenerateRequest
from app.ai.gemini_service import generate_code

router = APIRouter()


@router.post("/generate")
def generate(request: GenerateRequest):

    result = generate_code(

        code=request.code,

        language=request.language,

        title=request.title,

        url=request.url,

        page_context=request.page_context,

        platform=request.platform

    )

    return {

        "title": "AI Generated Solution",

        "analysis": result

    }