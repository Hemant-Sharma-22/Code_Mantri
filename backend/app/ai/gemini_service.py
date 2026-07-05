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

def generate_from_prompt_builder(
    prompt_builder,
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    prompt = prompt_builder(
        code=code,
        language=language,
        title=title,
        url=url,
        page_context=page_context,
        platform=platform
    )

    return generate(prompt)

def explain_code(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return generate_from_prompt_builder(

        build_prompt,

        code,

        language,

        title,

        url,

        page_context,

        platform

    )




def detect_bugs(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return generate_from_prompt_builder(

        build_bug_prompt,

        code,

        language,

        title,

        url,

        page_context,

        platform

    )



def optimize_code(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return generate_from_prompt_builder(

        build_optimize_prompt,

        code,

        language,

        title,

        url,

        page_context,

        platform

    )



def generate_comments(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return generate_from_prompt_builder(

        build_comments_prompt,

        code,

        language,

        title,

        url,

        page_context,

        platform

    )



def translate_code(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return generate_from_prompt_builder(

        build_translate_prompt,

        code,

        language,

        title,

        url,

        page_context,

        platform

    )


def analyze_complexity(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return generate_from_prompt_builder(

        build_complexity_prompt,

        code,

        language,

        title,

        url,

        page_context,

        platform

    )


def generate_tests(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return generate_from_prompt_builder(

        build_tests_prompt,

        code,

        language,

        title,

        url,

        page_context,

        platform

    )

