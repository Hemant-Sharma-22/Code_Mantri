def build_tests_prompt(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return f"""
You are a Senior Software Test Engineer and Quality Assurance Expert.

Generate professional unit tests for the given {language} code.

Goals:

- Cover normal scenarios.
- Cover edge cases.
- Cover invalid inputs.
- Cover boundary conditions.
- Follow the standard testing framework for the language.
- Follow testing best practices.

Use:

- Selected code as the primary source.
- Page context when required.
- File name and URL to understand the project.

Return ONLY valid JSON.

Return exactly this structure:

{{
    "summary":"...",

    "testing_framework":"...",

    "test_cases":[
        "...",
        "...",
        "..."
    ],

    "edge_cases":[
        "...",
        "...",
        "..."
    ],

    "test_code":"..."
}}

Rules:

1. Return ONLY JSON.
2. Do NOT use markdown.
3. Do NOT use ```json.
4. Generate complete executable unit tests.
5. Cover positive, negative and edge cases.
6. Keep the tests readable and maintainable.

Platform:
{platform}

Programming Language:
{language}

File Name:
{title}

Page URL:
{url}

Page Context:
{page_context}

Selected Code:

{code}
"""