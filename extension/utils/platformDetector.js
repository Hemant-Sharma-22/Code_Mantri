function detectPlatform(url) {

    url = url.toLowerCase();

    if (url.includes("github.com"))
        return "github";

    if (url.includes("leetcode.com"))
        return "leetcode";

    if (url.includes("geeksforgeeks.org"))
        return "geeksforgeeks";

    if (url.includes("codechef.com"))
        return "codechef";

    return "unknown";
}