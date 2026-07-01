import os
import json

from dotenv import load_dotenv
from google import genai
from app.prompts.complexity import build_complexity_prompt
from app.prompts.translate import build_translate_prompt
from app.prompts.comments import build_comments_prompt
from app.prompts.bugs import build_bug_prompt
from app.prompts.optimize import build_optimize_prompt
from app.prompts.router import build_prompt
from app.prompts.tests import build_tests_prompt

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

def detect_bugs(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    prompt = build_bug_prompt(
        code=code,
        language=language,
        title=title,
        url=url,
        page_context=page_context,
        platform=platform
    )

    return generate(prompt)

def optimize_code(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    prompt = build_optimize_prompt(
        code=code,
        language=language,
        title=title,
        url=url,
        page_context=page_context,
        platform=platform
    )

    return generate(prompt)

def generate_comments(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    prompt = build_comments_prompt(
        code=code,
        language=language,
        title=title,
        url=url,
        page_context=page_context,
        platform=platform
    )

    return generate(prompt)

def translate_code(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    prompt = build_translate_prompt(
        code=code,
        language=language,
        title=title,
        url=url,
        page_context=page_context,
        platform=platform
    )

    return generate(prompt)

def analyze_complexity(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    prompt = build_complexity_prompt(
        code=code,
        language=language,
        title=title,
        url=url,
        page_context=page_context,
        platform=platform
    )

    return generate(prompt)

def generate_tests(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    prompt = build_tests_prompt(
        code=code,
        language=language,
        title=title,
        url=url,
        page_context=page_context,
        platform=platform
    )

    return generate(prompt)