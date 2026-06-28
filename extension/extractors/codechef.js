export function extractCodeChef() {

    return {

        title: document.title,

        url: window.location.href,

        selectedText: window
            .getSelection()
            .toString()
            .trim()

    };

}