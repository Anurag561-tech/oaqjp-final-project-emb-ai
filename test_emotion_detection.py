from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotionalAnalyzer(unittest.TestCase):
    def test_emotion_analyzer(self):
        test1 = emotion_detector("I am glad this happened")
        test2 = emotion_detector("I am really mad about this")
        test3 = emotion_detector("I feel disgusted just hearing about this")
        test4 = emotion_detector("I am so sad about this")
        test5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test1, "joy")
        self.assertEqual(test1, "anger")
        self.assertEqual(test1, "disgust")
        
        self.assertEqual(test1, "sadness")
        self.assertEqual(test1, "fear")

if __name__ == "__main__":
    unittest.main()