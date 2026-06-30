def build_codechef_prompt(
    code,
    language,
    title="",
    url="",
    page_context=""
):

    return f"""
You are an expert Competitive Programmer.

The solution comes from CodeChef.

Focus on:

- Optimization
- Competitive Programming Tricks
- Constraints
- Time Complexity
- Space Complexity

Return valid JSON.

Selected Code:

{code}

Page Context:

{page_context}
"""