function analyzeBehavior(paragraph) {
    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ paragraph: paragraph })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('analysisResult').innerText = data.speed_analysis;
    })
    .catch(error => console.error('Error:', error));
}
