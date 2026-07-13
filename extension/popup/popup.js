document.addEventListener("DOMContentLoaded", async () => {
    
// let currentCode = "";

    console.log("AI Code Mentor Started");
    
    const explainButton =
    document.getElementById("explain-btn");

    const copyButton =
    document.getElementById("copy-btn");


    const optimizeButton =
    document.getElementById("optimize-btn");

    const generateButton =
    document.getElementById("generate-btn");

const bugsButton =
document.getElementById("bugs-btn");

const codeModal =
document.getElementById("code-modal");

const codeModalBody =
document.getElementById("code-modal-body");

const codeModalTitle =
document.getElementById("code-modal-title");

const closeCodeModal =
document.getElementById("close-code-modal");

const copyCodeButton =
document.getElementById("copy-code-btn");

optimizeButton.addEventListener("click", () => {

    runAIAction(
        "optimize",
        "Optimization completed."
    );

});

copyButton.addEventListener("click", async () => {

    const text =
        analysisResult.innerText;

    if (!text.trim()) {

        showStatus(
            "Nothing to copy.",
            "warning"
        );

        return;

    }

    await navigator.clipboard.writeText(text);

    showStatus(
        "Copied successfully.",
        "success"
    );

});

function openCodeModal(title, code) {

    codeModalTitle.textContent = title;

    codeModalBody.textContent = code;

    codeModal.classList.remove("hidden");

}

function closeModal() {

    codeModal.classList.add("hidden");

}

closeCodeModal.addEventListener("click", () => {

    closeModal();

});

copyCodeButton.addEventListener("click", async () => {

    await navigator.clipboard.writeText(

        codeModalBody.textContent

    );

    copyCodeButton.textContent =
        "✅ Copied";

    setTimeout(() => {

        copyCodeButton.textContent =
            "📋 Copy Code";

    }, 2000);

});

generateButton.addEventListener("click", () => {

    runAIAction(

        "generate",

        "Code generated successfully."

    );

});

const downloadButton =
document.getElementById("download-btn");

downloadButton.addEventListener("click", () => {

    const text =
        analysisResult.innerText;

    if (!text.trim()) {

        showStatus(
            "Nothing to download.",
            "warning"
        );

        return;

    }

    const blob = new Blob(

        [text],

        {

            type: "text/plain"

        }

    );

    const url =
        URL.createObjectURL(blob);

    const a =
        document.createElement("a");

    a.href = url;

    a.download = "ai-analysis.txt";

    a.click();

    URL.revokeObjectURL(url);

    showStatus(
        "Download completed.",
        "success"
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

function getItemTitle(section, index) {

    const titles = {

        bugs: "🐞 Bug",

        optimizations: "🚀 Optimization",

        test_cases: "🧪 Test Case",

        edge_cases: "⚠️ Edge Case",

        highlights: "💡 Highlight",

        bottlenecks: "🚧 Bottleneck",

        optimization_tips: "✨ Tip",

        best_practices: "📘 Best Practice",

        translation_notes: "🔄 Note"

    };

    return `${titles[section] || "📄 Item"} ${index + 1}`;

}

function renderJSONAnalysis(response) {

    pageTitle.textContent = response.title;
    pageURL.textContent = response.url;

    if (!response.selectedText) {

        selectedCode.textContent = "No text selected.";

        showStatus(
            "Please select some code first.",
            "warning"
        );

        return;
    }

    selectedCode.textContent = response.selectedText;

    if (response.analysis.error) {

        analysisResult.textContent =
            response.analysis.error;

        return;
    }

    let html = "";

    for (const key in response.analysis) {

        const value = response.analysis[key];

        html += `
            <h3>${formatHeading(key)}</h3>
        `;

        if (Array.isArray(value)) {

    value.forEach((item, index) => {

        if (typeof item === "object") {

            html += `
                <div class="result-item">
                    <h4>${getItemTitle(key, index)}</h4>
            `;

            for (const property in item) {

    if (property === "code") {

    html += `

        <div class="view-code-card">

            <button
                class="view-code-btn"
                data-code="${escapeHTML(item[property])}">

                👀 View Code

            </button>

        </div>

    `;

    continue;

}

    if (Array.isArray(item[property])) {

    html += `<ul>`;

    item[property].forEach(step => {

        html += `<li>${step}</li>`;

    });

    html += `</ul>`;

    continue;

}

html += `

<p>

<strong>${formatHeading(property)}:</strong>

${item[property]}

</p>

`;

}

            html += `</div>`;

        }
        else {

            html += `<li>${item}</li>`;

        }

    });

}

        else {

            const codeFields = [
                "code",

    "optimized_code",

    "translated_code",

    "commented_code",

    "corrected_code",

    "test_code"

];

if (codeFields.includes(key)) {

    currentCode = value;

    html += `

        <div class="view-code-card">

            <p>💻 Code Available</p>

            <button class="view-code-btn">

                👀 View Code

            </button>

        </div>

    `;

    continue;
}

else {

    html += `<p>${value}</p>`;

}

        }

    }

    analysisResult.innerHTML = html;

    document
    .querySelectorAll(".view-code-btn")
    .forEach(button => {

        button.addEventListener("click", () => {

            openCodeModal(

                "Generated Code",

                button.dataset.code

            );

        });

    });

}

function formatHeading(text) {

    return text
        .replaceAll("_", " ")
        .replace(/\b\w/g, c => c.toUpperCase());

}

function escapeHTML(text) {

    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");

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

            renderJSONAnalysis(response);

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