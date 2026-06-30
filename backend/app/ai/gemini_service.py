import os
import json

from dotenv import load_dotenv
from google import genai

from app.prompts.router import build_prompt

load_dotenv()

MODEL_NAME = "gemini-2.5-flash"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate(prompt):

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        text = response.text.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")

        return json.loads(text)

    except Exception as e:

        return {
            "error": str(e)
        }


def explain_code(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    prompt = build_prompt(
        platform=platform,
        code=code,
        language=language,
        title=title,
        url=url,
        page_context=page_context
    )

    return generate(prompt)