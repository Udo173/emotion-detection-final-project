import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test für Freude
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # Test für Wut
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # Test für Verzweiflung/Trauer
        result_3 = emotion_detector("I am so sad about this")
        self.assertEqual(result_3['dominant_emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()