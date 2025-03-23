import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers )
    response = json.loads(response.text)

    emotions = response.get('emotionPredictions')[0].get('emotion')
    anger_score = emotions.get('anger')
    disgust_score = emotions.get('disgust')
    fear_score = emotions.get('fear')
    joy_score = emotions.get('joy')
    sadness_score = emotions.get('sadness')

    formatted_response = {'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score}

    max_score = 0.0
    max_key = ''

    for key, value in formatted_response.items():
        if value > max_score:
            max_key = key
            max_score = value
    
    formatted_response['dominant_emotion'] = max_key
    
    return formatted_response