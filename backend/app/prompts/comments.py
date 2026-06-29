def build_comment_prompt(code: str, language: str):

    return f"""
Add professional comments to this {language} code.

Return only commented code.

Code:

{code}
"""