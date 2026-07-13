from pydantic import BaseModel


class GenerateRequest(BaseModel):

    language: str

    platform: str = ""

    code: str

    title: str = ""

    url: str = ""

    page_context: str = ""