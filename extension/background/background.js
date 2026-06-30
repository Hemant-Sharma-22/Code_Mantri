chrome.runtime.onInstalled.addListener(() => {
    console.log("AI Code Mentor Installed");
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

    if (message.action !== "analyze") {
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

                        const backendResponse = await fetch(
                            "http://127.0.0.1:8000/analyze",
                            {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json"
                                },
                               body: JSON.stringify({

    language: "java",

    code: response.selectedText,

    title: response.title,

    url: response.url,

    page_context: response.pageText

}) 
                            }
                        );

                        const aiResult = await backendResponse.json();

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