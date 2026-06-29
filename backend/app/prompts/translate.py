def build_translate_prompt(code: str, source: str, target: str):

    return f"""
Convert this {source} code into {target}.

Only return valid {target} code.

Code:

{code}
"""