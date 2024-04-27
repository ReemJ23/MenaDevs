document.getElementById("paragraph").addEventListener("input", function(event) {
    var paragraph = event.target.value.trim();
    
    if (paragraph.length === 0) {
        clearResult();
        return;
    }
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/analyze", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            updateResult(response.speed_analysis);
        }
    };
    var data = JSON.stringify({ "paragraph": paragraph });
    xhr.send(data);
});

function updateResult(result) {
    var resultElement = document.getElementById("result");
    resultElement.textContent = result;
    if (result.includes("Abnormal")) {
        resultElement.style.color = "red";
    } else {
        resultElement.style.color = "black";
    }
}

function clearResult() {
    document.getElementById("result").textContent = "";
}
