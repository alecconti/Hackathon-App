document.getElementById('image-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const fileInput = document.getElementById('image-file');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/classify-image', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
});

document.getElementById('chatbot-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const queryInput = document.getElementById('query');
    const response = await fetch('/rag-chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: queryInput.value })
    });
    const result = await response.json();
    document.getElementById('chatbot-response').innerText = JSON.stringify(result, null, 2);
});
