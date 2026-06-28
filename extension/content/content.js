chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

    if (message.action === "analyzePage") {

        const selectedText = window.getSelection().toString().trim();

        sendResponse({

            title: document.title,

            url: window.location.href,

            selectedText: selectedText,

            pageText: document.body.innerText.substring(0, 500)

        });

    }

    return true;

});