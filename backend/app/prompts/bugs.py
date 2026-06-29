def build_bug_prompt(code: str, language: str):

    return f"""
You are a Senior Software Engineer.

Find all bugs in this {language} code.

Return:

## Bugs

## Severity

## Fix

Code:

{code}
"""