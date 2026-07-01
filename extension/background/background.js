function detectLanguage(url, title) {

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

        `http://127.0.0.1:8000/${endpoint}`,

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
    message.action !== "tests"
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

let endpoint = "analyze";

if (message.action === "bugs") {

    endpoint = "bugs";

}

else if (message.action === "optimize") {

    endpoint = "optimize";

}

else if (message.action === "comments") {

    endpoint = "comments";

}

else if (message.action === "translate") {

    endpoint = "translate";

}
else if (message.action === "complexity") {

    endpoint = "complexity";

}
else if (message.action === "tests") {

    endpoint = "tests";

}

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