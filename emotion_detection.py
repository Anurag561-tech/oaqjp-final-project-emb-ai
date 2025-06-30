from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector
import requests, json

app = Flask("Emotion Analyzer", template_folder='templates')

@app.route("/emotionDetector")
def emotion_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    
    if not text_to_analyze:
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'message': "Invalid text! Please try again!"
        }), 400

    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=myobj, headers=headers)

   
    if response.status_code != 200:
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'message': "API error. Please try again later."
        }), response.status_code

   
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

    
    if not dominant_emotion:
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'message': "Invalid text! Please try again!"
        }), 400

    return jsonify({
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }), 200

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
