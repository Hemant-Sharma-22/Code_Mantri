from pydantic import BaseModel

class AnalyzeRequest(BaseModel):

    language: str

    platform: str = ""

    code: str

    title: str = ""

    url: str = ""

    page_context: str = ""

class AnalyzeResponse(BaseModel):
    success: bool
    message: str
    language: str
    lines: int