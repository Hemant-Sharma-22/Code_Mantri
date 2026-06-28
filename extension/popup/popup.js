document.addEventListener("DOMContentLoaded", async () => {

    console.log("AI Code Mentor Started");

    const analyzeButton = document.getElementById("analyze-btn");
    
    const pageTitle = document.getElementById("page-title");
    
    const pageURL = document.getElementById("page-url");
    const selectedCode = document.getElementById("selected-code");

    const statusMessage = document.getElementById("status-message");

function showStatus(message, type) {

    statusMessage.textContent = message;

    statusMessage.className = "";

    statusMessage.classList.add(type);

    setTimeout(() => {

        statusMessage.className = "hidden";

    }, 3000);
}

    const [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });

    pageTitle.textContent = tab.title;
    pageURL.textContent = tab.url;

analyzeButton.addEventListener("click", () => {

    chrome.runtime.sendMessage(
        {
            action: "analyze"
        },
        (response) => {

    if (chrome.runtime.lastError) {

        showStatus(
            "Unable to connect to the current page.",
            "error"
        );

        return;
    }

    if (!response) {

        showStatus(
            "No response received.",
            "error"
        );

        return;
    }

    pageTitle.textContent = response.title;
    pageURL.textContent = response.url;

    if (response.selectedText) {

        selectedCode.textContent = response.selectedText;

        showStatus(
            "Code extracted successfully.",
            "success"
        );

    } else {

        selectedCode.textContent =
            "No text selected.";

        showStatus(
            "Please select some code first.",
            "warning"
        );
    }

}
    );
});

});