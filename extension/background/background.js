chrome.runtime.onInstalled.addListener(() => {

    console.log("AI Code Mentor Installed");

});
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

    if (message.action === "analyze") {

        chrome.tabs.query(
            { active: true, currentWindow: true },
            (tabs) => {

                chrome.tabs.sendMessage(
                    tabs[0].id,
                    { action: "analyzePage" },
                    (response) => {

                        sendResponse(response);

                    }
                );

            }
        );

        return true;
    }

});