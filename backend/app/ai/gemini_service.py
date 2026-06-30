import os
import json

from dotenv import load_dotenv
from google import genai

from app.prompts.explain import build_explain_prompt

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


def explain_code(code, language):

    prompt = build_explain_prompt(
        code,
        language
    )

    return generate(prompt)