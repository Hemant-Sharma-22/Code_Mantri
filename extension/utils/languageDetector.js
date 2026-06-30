export function detectLanguage(url, title) {

    const text = (url + " " + title).toLowerCase();

    if (text.includes(".java")) return "java";
    if (text.includes(".py")) return "python";
    if (text.includes(".cpp")) return "cpp";
    if (text.includes(".c")) return "c";
    if (text.includes(".js")) return "javascript";
    if (text.includes(".ts")) return "typescript";
    if (text.includes(".cs")) return "csharp";
    if (text.includes(".go")) return "go";
    if (text.includes(".php")) return "php";
    if (text.includes(".rb")) return "ruby";
    if (text.includes(".kt")) return "kotlin";

    return "text";
}