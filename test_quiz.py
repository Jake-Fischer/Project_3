import quiz
import unittest

class TestQuiz(unittest.TestCase):

    # 
    def test_get_topics_and_number_of_questions(self):
        expected_dictionary = {'Animals':2, 'Sports':2, 'Literature':1}
        self.assertEqual(expected_dictionary, quiz.get_topics_and_number_of_questions())