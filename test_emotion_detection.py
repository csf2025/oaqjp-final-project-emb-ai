import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_correct_emotion(self):
        joy_statement = "I am glad this happened"
        anger_statement = "I am really mad about this"
        disgust_statement = "I feel disgusted just hearing about this"
        sadness_statement = "I am so sad about this"
        fear_statement = "I am really afraid that this will happen"

        self.assertEqual(str(emotion_detector(joy_statement).get('dominant_emotion')), "joy")

        self.assertEqual(str(emotion_detector(anger_statement).get('dominant_emotion')), "anger")

        self.assertEqual(str(emotion_detector(disgust_statement).get('dominant_emotion')), "disgust")

        self.assertEqual(str(emotion_detector(sadness_statement).get('dominant_emotion')), "sadness")

        self.assertEqual(str(emotion_detector(fear_statement).get('dominant_emotion')), "fear")

if __name__ == '__main__':
    unittest.main()