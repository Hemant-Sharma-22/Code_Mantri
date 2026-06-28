export function extractGitHub() {

    return {

        title: document.title,

        url: window.location.href,

        selectedText: window
            .getSelection()
            .toString()
            .trim()

    };

}