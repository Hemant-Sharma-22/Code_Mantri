def build_optimize_prompt(code: str, language: str):

    return f"""
You are a Performance Engineer.

Optimize this {language} code.

Return:

## Optimized Code

## Improvements

## Time Complexity

## Space Complexity

Code:

{code}
"""