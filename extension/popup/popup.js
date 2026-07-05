document.addEventListener("DOMContentLoaded", async () => {
    
    console.log("AI Code Mentor Started");
    
    const explainButton =
    document.getElementById("explain-btn");

    const optimizeButton =
    document.getElementById("optimize-btn");

const bugsButton =
document.getElementById("bugs-btn");

optimizeButton.addEventListener("click", () => {

    runAIAction(
        "optimize",
        "Optimization completed."
    );

});


const commentsButton =
document.getElementById("comments-btn");

commentsButton.addEventListener("click", () => {

    runAIAction(
        "comments",
        "Comments generated successfully."
    );

});

const translateButton =
document.getElementById("translate-btn");

translateButton.addEventListener("click", () => {

    runAIAction(
        "translate",
        "Translation completed."
    );

});

const complexityButton =
document.getElementById("complexity-btn");

complexityButton.addEventListener("click", () => {

    runAIAction(
        "complexity",
        "Complexity analysis completed."
    );

});


const testsButton =
document.getElementById("tests-btn");

testsButton.addEventListener("click", () => {

    runAIAction(
        "tests",
        "Unit tests generated."
    );

});
  
    const pageTitle = document.getElementById("page-title");
    
    const pageURL = document.getElementById("page-url");
    const selectedCode = document.getElementById("selected-code");
    const analysisResult = document.getElementById("analysis-result");
    const statusMessage = document.getElementById("status-message");


bugsButton.addEventListener("click", () => {

    runAIAction(
        "bugs",
        "Bug detection completed."
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

function setLoading(isLoading) {

    document
        .querySelectorAll(".action-buttons button")
        .forEach(button => {

            button.disabled = isLoading;

        });

}

function runAIAction(action, successMessage) {
    
    setLoading(true);

    chrome.runtime.sendMessage(
        {
            action
        },
        (response) => {

            if (chrome.runtime.lastError) {

                setLoading(false);

                showStatus(
                    "Unable to connect.",
                    "error"
                );

                return;
            }

            if (!response) {

                setLoading(false);

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

            setLoading(false);

            showStatus(
                successMessage,
                "success"
            );

        }
    );

}

function renderExplainAnalysis(response) {

    pageTitle.textContent = response.title;
    pageURL.textContent = response.url;

    if (!response.selectedText) {
        setLoading(false);
        selectedCode.textContent = "No text selected.";

        showStatus(
            "Please select some code first.",
            "warning"
        );

        return;
    }

    selectedCode.textContent = response.selectedText;

    if (response.analysis.error) {
        setLoading(false);
        analysisResult.textContent =
            JSON.stringify(response.analysis.error, null, 2);

        return;
    }

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

        <p><strong>Time:</strong>
            ${response.analysis.time_complexity}
        </p>

        <p><strong>Space:</strong>
            ${response.analysis.space_complexity}
        </p>
    `;
    setLoading(false);

    showStatus(
        "AI analysis completed.",
        "success"
    );
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
                    "Unable to connect.",
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

            renderExplainAnalysis(response);

        }
    );

});

});