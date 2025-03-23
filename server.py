from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def display_init_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotions():
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!",400

    else:
        response = emotion_detector(text_to_analyze)
        anger_score = response.get('anger')
        disgust_score = response.get('disgust')
        fear_score = response.get('fear')
        joy_score = response.get('joy')
        sadness_score = response.get('sadness')
        dominant_emotion = response.get('dominant_emotion')

        formatted_response = f"""For the given statement, the system response is 'anger': {anger_score},
        'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and
        'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."""
        
        return formatted_response

app.run(host='127.0.0.1', port = 5001, debug = True)