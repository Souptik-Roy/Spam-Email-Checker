document.getElementById("check-btn").addEventListener("click", async () => {
    const message = document.getElementById("message").value;
    const resultEl = document.getElementById("result");
    resultEl.textContent = "Checking...";
    resultEl.className = "result-box checking";

    try {
        const response = await fetch("https://spam-backend-zpw7.onrender.com/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        if (response.ok) {
            if (data.prediction === "Spam") {
                resultEl.textContent = "🚨 This looks like Spam!";
                resultEl.className = "result-box spam";
            } else {
                resultEl.textContent = "✅ This message is Not Spam.";
                resultEl.className = "result-box not-spam";
            }
        } else {
            resultEl.textContent = "⚠️ " + data.error;
            resultEl.className = "result-box checking";
        }
    } catch (err) {
        resultEl.textContent = "⚠️ Error connecting to server.";
        resultEl.className = "result-box checking";
    }
});
