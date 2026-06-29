def build_translate_prompt(
    code: str,
    source: str,
    target: str
):

    return f"""
Convert the following {source} code into {target}.

Return ONLY the converted code.

Code:

{code}
"""