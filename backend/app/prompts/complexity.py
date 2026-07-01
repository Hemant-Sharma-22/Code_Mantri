def build_complexity_prompt(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return f"""
You are an expert Software Engineer.

Analyze ONLY the algorithmic complexity of this {language} code.

Return ONLY valid JSON.

Return exactly this structure:

{{
    "summary":"...",

    "time_complexity":"...",

    "space_complexity":"...",

    "explanation":"..."
}}

Do not return markdown.

Platform:
{platform}

File:
{title}

URL:
{url}

Context:
{page_context}

Selected Code:

{code}
"""