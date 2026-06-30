def build_explain_prompt(code: str, language: str):

    return f"""
You are an expert software engineer.

Analyze this {language} code.

Return ONLY valid JSON in exactly this format:

{{
    "summary": "...",
    "suggestions": [
        "...",
        "...",
        "..."
    ],
    "time_complexity": "...",
    "space_complexity": "..."
}}

Do not include markdown.
Do not include ```json.
Do not include explanations outside JSON.

Code:
{code}
"""