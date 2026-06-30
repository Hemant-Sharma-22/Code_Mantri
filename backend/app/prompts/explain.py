def build_explain_prompt(
    code,
    language,
    title="",
    url="",
    page_context=""
):

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

File Name:
{title}

Page URL:
{url}

Page Context:
{page_context}

Selected Code:
{code}
"""