import os
import time

from dotenv import load_dotenv
from google import genai
from app.prompts.explain import build_explain_prompt

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate(prompt):

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt
            )

            return response.text

        except Exception as e:

            if attempt == 2:
                return f"AI Error: {str(e)}"

            time.sleep(2)

def explain_code(code, language):

    prompt = build_explain_prompt(
        code,
        language
    )

    return generate(prompt)


































# def explain_code(code: str, language: str):

#     prompt = f"""
# You are a Senior Software Engineer.

# Analyze this {language} code.

# Return your answer in the following format:

# Summary:
# ...

# Suggestions:
# - ...
# - ...

# Time Complexity:
# ...

# Space Complexity:
# ...

# Code:

# {code}
# """

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=prompt,
#     )

#     return response.text
