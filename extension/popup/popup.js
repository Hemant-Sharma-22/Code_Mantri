document.addEventListener("DOMContentLoaded", async () => {

    console.log("AI Code Mentor Started");

    const analyzeButton = document.getElementById("analyze-btn");
    
    const pageTitle = document.getElementById("page-title");
    
    const pageURL = document.getElementById("page-url");
    const selectedCode = document.getElementById("selected-code");

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

            console.log(response);

            pageTitle.textContent = response.title;

            pageURL.textContent = response.url;

            if(response.selectedText){

                selectedCode.textContent = response.selectedText;
            }
            else{

                selectedCode.textContent =
                "No text selected.";
            }
        }
    );
});

});