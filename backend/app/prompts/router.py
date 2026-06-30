from app.prompts.explain import build_explain_prompt
from app.prompts.github_prompt import build_github_prompt
from app.prompts.leetcode_prompt import build_leetcode_prompt
from app.prompts.codechef_prompt import build_codechef_prompt


def build_prompt(
    platform,
    code,
    language,
    title,
    url,
    page_context
):

    if platform == "github":

        return build_github_prompt(
            code,
            language,
            title,
            url,
            page_context
        )

    elif platform == "leetcode":

        return build_leetcode_prompt(
            code,
            language,
            title,
            url,
            page_context
        )

    elif platform == "codechef":

        return build_codechef_prompt(
            code,
            language,
            title,
            url,
            page_context
        )

    return build_explain_prompt(
        code,
        language,
        title,
        url,
        page_context,
        platform
    )