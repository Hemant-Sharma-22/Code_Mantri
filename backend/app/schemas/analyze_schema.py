from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    language: str
    code: str


class AnalyzeResponse(BaseModel):
    success: bool
    message: str
    language: str
    lines: int