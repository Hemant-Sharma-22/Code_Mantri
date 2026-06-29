def build_bug_prompt(code: str, language: str):

    return f"""
You are a Senior Software Engineer.

Find all possible bugs in this {language} code.

Return in Markdown.

## Bugs

## Severity

## Fix

Code:

{code}
"""