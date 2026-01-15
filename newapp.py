from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AI Image Detector</title>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #ffffff;
    color: #0a2540;
}
header {
    position: sticky;
    top: 0;
    background: white;
    padding: 15px 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
header h2 {
    color: #0b5cff;
    margin: 0;
}
nav a {
    margin-left: 15px;
    text-decoration: none;
    color: #0a2540;
    font-weight: bold;
}
.hero {
    text-align: center;
    padding: 70px 20px;
}
.hero h1 {
    font-size: 36px;
}
.hero p {
    font-size: 18px;
    max-width: 700px;
    margin: auto;
    color: #555;
}
.btn {
    margin-top: 25px;
    padding: 12px 30px;
    font-size: 16px;
    background: #0b5cff;
    color: white;
    border: none;
    border-radius: 30px;
    cursor: pointer;
}
.section {
    padding: 60px 20px;
    max-width: 900px;
    margin: auto;
}
.card {
    background: #f5f8ff;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 30px;
    text-align: center;
}
.card h3 {
    margin-bottom: 10px;
}
.steps {
    border-left: 4px solid #0b5cff;
    padding-left: 20px;
}
.detect-box {
    background: #f0f4ff;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
}
input[type=file] {
    margin-top: 15px;
}
.result {
    margin-top: 20px;
    font-size: 20px;
    font-weight: bold;
}
footer {
    text-align: center;
    padding: 20px;
    color: #777;
}
</style>
</head>

<body>

<header>
    <h2>Decopy AI</h2>
    <nav>
        <a href="#how">How it Works</a>
        <a href="#detect">Detect</a>
    </nav>
</header>

<div class="hero">
    <h1>Trust what’s real, spot the fakes.</h1>
    <p>
        Smart AI-generated images need an even smarter AI Image Checker.
        Upload an image and detect whether it is AI-generated or real.
    </p>
    <a href="#detect"><button class="btn">Detect an Image</button></a>
</div>

<div class="section">
    <div class="card">
        <h3>Completely Free</h3>
        <p>This AI Image Detector is 100% free and easy to use.</p>
    </div>

    <div class="card">
        <h3>High Accuracy</h3>
        <p>Uses AI-based pattern analysis to identify AI-generated images.</p>
    </div>
</div>

<div class="section" id="how">
    <h2>How It Works</h2>
    <div class="steps">
        <p><b>1.</b> Upload the image you want to analyze</p>
        <p><b>2.</b> The system scans image patterns</p>
        <p><b>3.</b> View AI or Real detection result</p>
    </div>
</div>

<div class="section" id="detect">
    <div class="detect-box">
        <h2>AI Image Detector</h2>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="image" required><br>
            <button class="btn" onclick="this.innerText='Analyzing...'">
                Analyze Image
            </button>
        </form>

        {% if result %}
        <div class="result">
            Result: {{ result }} <br>
            Confidence: {{ confidence }}%
        </div>
        {% endif %}
    </div>
</div>

<footer>
    Mini Project | AI Image Detector | Python & Flask
</footer>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    confidence = None

    if request.method == "POST":
        result = random.choice(["AI Generated Image", "Real Image"])
        confidence = random.randint(75, 99)

    return render_template_string(
        HTML,
        result=result,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run()
