def build_explain_prompt(code: str, language: str):

    return f"""
You are a Senior Software Engineer.

Analyze the following {language} code.

Return your answer in Markdown format.

## Summary
Explain what the code does.

## Suggestions
Give 3-5 improvements.

## Time Complexity

## Space Complexity

Code:

{code}
"""