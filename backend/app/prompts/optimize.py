def build_optimize_prompt(code: str, language: str):

    return f"""
Optimize this {language} code.

Return:

## Optimized Code

## Improvements

## Time Complexity

## Space Complexity

Code:

{code}
"""