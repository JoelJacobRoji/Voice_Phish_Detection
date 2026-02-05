const analyzeBtn = document.getElementById("analyzeBtn");
const audioInput = document.getElementById("audioFile");

const progressBar = document.getElementById("progress-bar");
const progressContainer = document.getElementById("progressContainer");
const statusText = document.getElementById("statusText");

const resultDiv = document.getElementById("result");
const riskLevel = document.getElementById("riskLevel");
const riskScore = document.getElementById("riskScore");
const reasonList = document.getElementById("reasonList");
const transcriptText = document.getElementById("transcriptText");
const fileLabel = document.getElementById("fileLabel");

/**
 * ✅ DEPLOYMENT-SAFE BACKEND URL
 * - Works on localhost
 * - Works after deployment (same domain)
 */
const BACKEND_URL = `${window.location.protocol}//${window.location.hostname}:8000/analyze-audio`;

audioInput.addEventListener("change", () => {
    if (audioInput.files.length) {
        fileLabel.innerText = audioInput.files[0].name;
    }
});

analyzeBtn.addEventListener("click", async () => {
    if (!audioInput.files.length) {
        alert("Please select an audio file");
        return;
    }

    // --------------------
    // Reset UI
    // --------------------
    resultDiv.classList.add("hidden");
    progressContainer.classList.remove("hidden");
    statusText.classList.remove("hidden");

    progressBar.style.width = "5%";
    statusText.innerText = "Uploading audio...";

    const formData = new FormData();
    formData.append("file", audioInput.files[0]);

    try {
        // --------------------
        // Upload
        // --------------------
        progressBar.style.width = "25%";

        const response = await fetch(BACKEND_URL, {
            method: "POST",
            body: formData
        });

        progressBar.style.width = "60%";
        statusText.innerText = "Analyzing content...";

        if (!response.ok) {
            throw new Error(`Backend returned ${response.status}`);
        }

        const data = await response.json();

        // --------------------
        // Finalize
        // --------------------
        progressBar.style.width = "100%";
        statusText.innerText = "Analysis complete";

        // --------------------
        // Risk Level & Score
        // --------------------
        riskLevel.innerText = `Risk Level: ${data.risk_level}`;
        riskScore.innerText = `${data.risk_score}%`;

        if (data.risk_level === "High") {
            riskLevel.style.color = "#ff5252";
        } else if (data.risk_level === "Medium") {
            riskLevel.style.color = "#ffca28";
        } else {
            riskLevel.style.color = "#66bb6a";
        }

        // --------------------
        // Matched Scam Phrases
        // --------------------
        reasonList.innerHTML = "";

        if (!data.matched_phrases || data.matched_phrases.length === 0) {
            const li = document.createElement("li");
            li.innerText = "No suspicious phrases detected";
            reasonList.appendChild(li);
        } else {
            data.matched_phrases.forEach(phrase => {
                const li = document.createElement("li");
                li.innerText = phrase;
                reasonList.appendChild(li);
            });
        }

        // --------------------
        // Transcript
        // --------------------
        transcriptText.innerText = data.transcript || "No transcript available";

        // --------------------
        // Show results
        // --------------------
        resultDiv.classList.remove("hidden");

    } catch (err) {
        console.error("Analysis failed:", err);
        alert("Failed to analyze audio. Backend is running, but analysis failed.");

        progressBar.style.width = "0%";
        statusText.classList.add("hidden");
    }
});
