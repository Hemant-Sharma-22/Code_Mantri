def build_github_prompt(
    code,
    language,
    title="",
    url="",
    page_context=""
):

    return f"""
You are a Senior Software Engineer.

The code comes from GitHub.

Focus on:

- Code quality
- Readability
- Design
- Best Practices
- Time Complexity

Return valid JSON.

Selected Code:

{code}

Page Context:

{page_context}
"""