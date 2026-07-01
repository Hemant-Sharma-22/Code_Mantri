def build_github_prompt(
    code,
    language,
    title="",
    url="",
    page_context=""
):

    return f"""
You are a Senior Software Engineer.

The following code comes from GitHub.

Focus on:

- Code quality
- Readability
- Best practices
- Design
- Time complexity
- Space complexity

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

Rules:
1. Return ONLY JSON.
2. Do NOT use markdown.
3. Do NOT use ```json.
4. Do NOT wrap the JSON inside another object like "code_review".

File Name:
{title}

Page URL:
{url}

Page Context:
{page_context}

Selected Code:
{code}
"""