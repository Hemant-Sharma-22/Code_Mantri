def build_translate_prompt(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return f"""
You are an expert software engineer.

Translate the following {language} code into another programming language.

Requirements:

- Preserve the same logic.
- Follow best coding practices.
- Keep the translated code readable.
- Do not change the algorithm.

Return ONLY valid JSON.

Return exactly this format:

{{
    "summary": "...",
    "target_language": "...",
    "translated_code": "..."
}}

Do not return markdown.
Do not use ```.

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