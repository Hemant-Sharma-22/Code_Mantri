export function detectPlatform() {

    const host = window.location.hostname;

    if (host.includes("github.com"))
        return "github";

    if (host.includes("leetcode.com"))
        return "leetcode";

    if (host.includes("codechef.com"))
        return "codechef";

    if (host.includes("geeksforgeeks.org"))
        return "gfg";

    if (host.includes("hackerrank.com"))
        return "hackerrank";

    return "generic";

}