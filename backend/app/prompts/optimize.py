def build_optimize_prompt(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return f"""
You are a Senior Software Performance Engineer and Code Reviewer.

Your goal is to optimize the given {language} code while explaining every important improvement.

Analyze the selected code considering:

- Performance
- Readability
- Memory usage
- Thread Safety (if applicable)
- Maintainability
- Best Practices

Return ONLY valid JSON.

Return exactly this structure:

{{
    "summary": "...",

    "overall_improvement": "...",

    "optimizations": [

        {{
            "title": "...",
            "reason": "...",
            "impact": "..."
        }}

    ],

    "optimized_code": "...",

    "best_practices": [

        "...",
        "...",
        "..."

    ]

}}

Rules:

1. Return ONLY JSON.
2. Do NOT use markdown.
3. Do NOT use ```json.
4. Preserve the original functionality.
5. Never remove required logic.
6. Explain every optimization in simple language.
7. Return complete optimized code.

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