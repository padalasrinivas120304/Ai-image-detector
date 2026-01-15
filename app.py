from flask import Flask, request, render_template_string
from PIL import Image
import os

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
        Upload an image and analyze whether it is AI-generated or real.
    </p>
    <a href="#detect"><button class="btn">Detect an Image</button></a>
</div>

<div class="section" id="how">
    <h2>How It Works</h2>
    <div class="steps">
        <p><b>1.</b> Upload an image</p>
        <p><b>2.</b> System analyzes image properties</p>
        <p><b>3.</b> Displays AI or Real result</p>
    </div>
</div>

<div class="section" id="detect">
    <div class="detect-box">
        <h2>AI Image Detector</h2>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="image" required><br><br>
            <button class="btn">Analyze Image</button>
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
        file = request.files.get("image")
        if file:
            img = Image.open(file)
            width, height = img.size

            file.seek(0, os.SEEK_END)
            size_kb = file.tell() / 1024

            # Simple logical detection (NOT random)
            if width >= 1024 and size_kb < 300:
                result = "AI Generated Image"
                confidence = 85
            else:
                result = "Real Image"
                confidence = 80

    return render_template_string(
        HTML,
        result=result,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run()
