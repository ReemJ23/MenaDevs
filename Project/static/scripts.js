function analyzeBehavior() {
    var paragraph = document.getElementById('paragraphInput').value;

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ paragraph: paragraph })
    })
    .then(response => response.json())
    .then(data => {
        var analysisResult = 'Typing Speed: ' + data.speed_analysis + '<br>' +
                             'Paragraph Content: ' + data.paragraph_analysis;
        document.getElementById('analysisResult').innerHTML = analysisResult;
    })
    .catch(error => console.error('Error:', error));
}
