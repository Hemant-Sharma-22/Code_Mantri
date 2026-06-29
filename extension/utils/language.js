function detectLanguage(url) {

    if(url.includes("leetcode"))
        return "java";

    if(url.includes("github"))
        return "unknown";

    if(url.includes("codechef"))
        return "cpp";

    return "text";

}

export { detectLanguage };