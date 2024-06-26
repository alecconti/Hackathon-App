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
    displayResults(result, URL.createObjectURL(fileInput.files[0]));
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
    const messageElement = document.createElement('div');
    messageElement.textContent = result.answer;
    document.getElementById('chatbot-messages').appendChild(messageElement);
});

function displayResults(result, imageUrl) {
    document.getElementById('input-image-display').src = imageUrl;
    // Assuming predictive image is available as a URL in the result
    document.getElementById('predictive-image-display').src = result.predictiveImageUrl || imageUrl;

    const diseaseList = document.getElementById('disease-list');
    diseaseList.innerHTML = '';
    result.diseases.forEach(disease => {
        const li = document.createElement('li');
        li.innerHTML = `<span>${disease.name}</span><span class="risk">${disease.risk}</span>`;
        diseaseList.appendChild(li);
    });
}
