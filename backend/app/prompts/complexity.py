def build_complexity_prompt(
    code,
    language,
    title="",
    url="",
    page_context="",
    platform=""
):

    return f"""
You are a Senior Software Engineer and Algorithm Expert.

Analyze ONLY the algorithmic complexity of the given {language} code.

Focus on:

- Time Complexity
- Space Complexity
- The reason behind each complexity
- Performance bottlenecks
- Possible optimizations

Use:

- Selected code as the primary source.
- Page context when required.
- File name and URL to understand the project.

Return ONLY valid JSON.

Return exactly this structure:

{{
    "summary":"...",

    "time_complexity":"...",

    "space_complexity":"...",

    "explanation":"...",

    "bottlenecks":[
        "...",
        "...",
        "..."
    ],

    "optimization_tips":[
        "...",
        "...",
        "..."
    ]
}}

Rules:

1. Return ONLY JSON.
2. Do NOT use markdown.
3. Do NOT use ```json.
4. Analyze the dominant algorithm only.
5. Explain complexities in simple language.
6. Mention practical optimization opportunities if applicable.

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