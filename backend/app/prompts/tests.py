def build_tests_prompt(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return f"""
You are an expert Software Test Engineer.

Generate high-quality unit tests for the given {language} code.

Requirements:

- Cover normal cases.
- Cover edge cases.
- Cover invalid inputs.
- Follow best practices.
- Use the standard testing framework for the language.

Return ONLY valid JSON.

Return exactly this format:

{{
    "summary":"...",

    "testing_framework":"...",

    "test_code":"..."
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