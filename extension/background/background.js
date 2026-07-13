const API_BASE_URL =
    "http://127.0.0.1:8000";

const LANGUAGE_MAP = {
    ".java": "java",
    ".py": "python",
    ".cpp": "cpp",
    ".c": "c",
    ".js": "javascript",
    ".ts": "typescript",
    ".cs": "csharp",
    ".go": "go",
    ".php": "php",
    ".rb": "ruby",
    ".kt": "kotlin"
};

const ENDPOINT_MAP = {
    analyze: "analyze",
    bugs: "bugs",
    optimize: "optimize",
    comments: "comments",
    translate: "translate",
    complexity: "complexity",
    tests: "tests",
    generate: "generate"
};

function detectLanguage(url, title) {

    const text = (url + " " + title).toLowerCase();

    for (const extension in LANGUAGE_MAP) {

    if (text.includes(extension)) {

        return LANGUAGE_MAP[extension];

    }

}

    return "text";

}

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

async function callBackend(endpoint, payload) {

    const response = await fetch(

        `${API_BASE_URL}/${endpoint}`,

        {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(payload)

        }

    );

    return await response.json();

}

chrome.runtime.onInstalled.addListener(() => {
    console.log("AI Code Mentor Installed");
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

if (
    message.action !== "analyze" &&
    message.action !== "bugs" &&
    message.action !== "optimize" &&
    message.action !== "comments" &&
    message.action !== "translate" &&
    message.action !== "complexity" &&
    message.action !== "tests" &&
    message.action !== "generate"
) {
    return;
}

    chrome.tabs.query(
        {
            active: true,
            currentWindow: true
        },
        (tabs) => {

            chrome.tabs.sendMessage(
                tabs[0].id,
                {
                    action: "analyzePage"
                },
                async (response) => {

                    if (chrome.runtime.lastError) {
                        sendResponse({
                            error: chrome.runtime.lastError.message
                        });
                        return;
                    }

                    if (!response) {
                        sendResponse({
                            error: "No response from content script."
                        });
                        return;
                    }

                    try {

                        const payload = {

    language: detectLanguage(
        response.url,
        response.title
    ),

    platform: detectPlatform(
        response.url
    ),

    code: response.selectedText,

    title: response.title,

    url: response.url,

    page_context: response.pageText

};



const endpoint = ENDPOINT_MAP[message.action];

const aiResult = await callBackend(

    endpoint,

    payload

);
console.log("AI RESULT:", aiResult);

sendResponse({

    title: response.title,

    url: response.url,

    selectedText: response.selectedText,

    analysis: aiResult.analysis

                        });

                    } catch (error) {

                        sendResponse({

                            error: error.message

                        });

                    }

                }
            );

        }
    );

    return true;

});