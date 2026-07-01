def build_bug_prompt(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return f"""
You are an expert Senior Software Engineer and Code Reviewer.

Platform:
{platform}

Programming Language:
{language}

Your task is to find bugs in the selected code.

Use:
- Selected code as the primary source.
- Page context if required.
- File name and URL to understand the project.

Return ONLY valid JSON.

Return exactly this structure:

{{
    "bugs": [
        {{
            "title": "...",
            "severity": "...",
            "description": "...",
            "fix": "..."
        }}
    ]
}}

Rules:

1. Return only JSON.
2. No markdown.
3. No explanations.
4. If there are no bugs, return:

{{
    "bugs":[]
}}

File Name:
{title}

URL:
{url}

Page Context:
{page_context}

Selected Code:

{code}
"""