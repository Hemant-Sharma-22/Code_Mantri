const BASE_URL = "http://127.0.0.1:8000";

async function analyzeCode(language, code) {

    const response = await fetch(`${BASE_URL}/analyze`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            language,
            code
        })

    });

    return await response.json();

}

export { analyzeCode };