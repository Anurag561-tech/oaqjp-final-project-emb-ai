"""
Flask server for Emotion Analyzer web application.
Receives user input, calls Watson NLP API for emotion detection,
and returns structured emotion data or error messages.
"""

import json
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer", template_folder='templates')

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Handles emotion detection requests.
    Returns emotion analysis in JSON format or an error message for invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!", 200

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 200

    return json.dumps(result), 200


@app.route("/")
def render_index_page():
    """
    Renders the index.html page for user input.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
