def build_leetcode_prompt(
    code,
    language,
    title="",
    url="",
    page_context=""
):

    return f"""
You are an expert DSA Mentor.

The code comes from LeetCode.

Focus on:

- Algorithm
- Logic
- Dry Run
- Time Complexity
- Space Complexity
- Better Approach

Return valid JSON.

Selected Code:

{code}

Page Context:

{page_context}
"""