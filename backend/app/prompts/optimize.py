def build_optimize_prompt(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return f"""
You are an expert software performance engineer.

Analyze this {language} code.

Your job is to improve:

- Performance
- Readability
- Memory usage
- Best Practices

Return ONLY valid JSON.

Return exactly this structure:

{{
    "summary":"...",

    "optimizations":[
        "...",
        "...",
        "..."
    ],

    "optimized_code":"..."
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