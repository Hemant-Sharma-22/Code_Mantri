document.addEventListener("DOMContentLoaded", async () => {
    
    console.log("AI Code Mentor Started");
    
    const explainButton =
    document.getElementById("explain-btn");

    const optimizeButton =
    document.getElementById("optimize-btn");

const bugsButton =
document.getElementById("bugs-btn");

optimizeButton.addEventListener("click", () => {

    chrome.runtime.sendMessage(
        {
            action: "optimize"
        },
        (response) => {

            if (chrome.runtime.lastError) {

                showStatus(
                    "Unable to connect.",
                    "error"
                );

                return;
            }

            if (!response) {

                showStatus(
                    "No response.",
                    "error"
                );

                return;
            }

            pageTitle.textContent = response.title;
            pageURL.textContent = response.url;
            selectedCode.textContent = response.selectedText;

            analysisResult.textContent =
                JSON.stringify(response.analysis, null, 2);

            showStatus(
                "Optimization completed.",
                "success"
            );

        }
    );

});


const commentsButton =
document.getElementById("comments-btn");

commentsButton.addEventListener("click", () => {

    chrome.runtime.sendMessage(
        {
            action: "comments"
        },
        (response) => {

            if (chrome.runtime.lastError) {

                showStatus(
                    "Unable to connect.",
                    "error"
                );

                return;
            }

            if (!response) {

                showStatus(
                    "No response.",
                    "error"
                );

                return;
            }

            pageTitle.textContent = response.title;
            pageURL.textContent = response.url;
            selectedCode.textContent = response.selectedText;

            analysisResult.textContent =
                JSON.stringify(response.analysis, null, 2);

            showStatus(
                "Comments generated successfully.",
                "success"
            );

        }
    );

});

const translateButton =
document.getElementById("translate-btn");

translateButton.addEventListener("click", () => {

    chrome.runtime.sendMessage(
        {
            action: "translate"
        },
        (response) => {

            if (chrome.runtime.lastError) {

                showStatus(
                    "Unable to connect.",
                    "error"
                );

                return;
            }

            if (!response) {

                showStatus(
                    "No response.",
                    "error"
                );

                return;
            }

            pageTitle.textContent = response.title;
            pageURL.textContent = response.url;
            selectedCode.textContent = response.selectedText;

            analysisResult.textContent =
                JSON.stringify(response.analysis, null, 2);

            showStatus(
                "Translation completed.",
                "success"
            );

        }
    );

});

const complexityButton =
document.getElementById("complexity-btn");

complexityButton.addEventListener("click", () => {

    chrome.runtime.sendMessage(
        {
            action: "complexity"
        },
        (response) => {

            if (chrome.runtime.lastError) {

                showStatus(
                    "Unable to connect.",
                    "error"
                );

                return;

            }

            if (!response) {

                showStatus(
                    "No response.",
                    "error"
                );

                return;

            }

            pageTitle.textContent = response.title;
            pageURL.textContent = response.url;
            selectedCode.textContent = response.selectedText;

            analysisResult.textContent =
                JSON.stringify(response.analysis, null, 2);

            showStatus(
                "Complexity analysis completed.",
                "success"
            );

        }

    );

});


const testsButton =
document.getElementById("tests-btn");

testsButton.addEventListener("click", () => {

    chrome.runtime.sendMessage(
        {
            action: "tests"
        },
        (response) => {

            if (chrome.runtime.lastError) {

                showStatus(
                    "Unable to connect.",
                    "error"
                );

                return;

            }

            if (!response) {

                showStatus(
                    "No response.",
                    "error"
                );

                return;

            }

            pageTitle.textContent = response.title;
            pageURL.textContent = response.url;
            selectedCode.textContent = response.selectedText;

            analysisResult.textContent =
                JSON.stringify(response.analysis, null, 2);

            showStatus(
                "Unit tests generated.",
                "success"
            );

        }

    );

});


    
    const pageTitle = document.getElementById("page-title");
    
    const pageURL = document.getElementById("page-url");
    const selectedCode = document.getElementById("selected-code");
    const analysisResult = document.getElementById("analysis-result");
    const statusMessage = document.getElementById("status-message");


    bugsButton.addEventListener("click", () => {

    chrome.runtime.sendMessage(

        {

            action: "bugs"

        },

        (response) => {

            if (chrome.runtime.lastError) {

                showStatus(

                    "Unable to connect.",

                    "error"

                );

                return;

            }

            if (!response) {

                showStatus(

                    "No response.",

                    "error"

                );

                return;

            }

            pageTitle.textContent = response.title;

            pageURL.textContent = response.url;

            selectedCode.textContent = response.selectedText;

            analysisResult.textContent =
                JSON.stringify(response.analysis, null, 2);

            showStatus(

                "Bug detection completed.",

                "success"

            );

        }

    );

});

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

explainButton.addEventListener("click", () => {

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

    if (response.analysis.error) {

        analysisResult.textContent =
            JSON.stringify(response.analysis.error, null, 2);

    } else {

        analysisResult.innerHTML = `
            <h3>📝 Summary</h3>
            <p>${response.analysis.summary}</p>

            <h3>💡 Suggestions</h3>
            <ul>
                ${response.analysis.suggestions
                    .map(item => `<li>${item}</li>`)
                    .join("")}
            </ul>

            <h3>⚡ Complexity</h3>

            <p><strong>Time:</strong> ${response.analysis.time_complexity}</p>

            <p><strong>Space:</strong> ${response.analysis.space_complexity}</p>
        `;
    }

    showStatus(
        "AI analysis completed.",
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