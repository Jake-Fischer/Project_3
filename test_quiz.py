import quiz
import unittest

class TestQuiz(unittest.TestCase):


    def test_get_topics_and_number_of_questions(self):
        expected_dictionary = {'Animals':2, 'Sports':2, 'Literature':1}
        self.assertEqual(expected_dictionary, quiz.get_topics_and_number_of_questions())


    def test_get_quiz_questions(self):
        expected_list = [{'id': 2, 'category': 'Sports', 'question_text': 'How many rings are on the Olympic flag?', 'correct_answer': '5', 'wrong_answer1': 'None', 'wrong_answer2': '4', 'wrong_answer3': '7', 'difficulty': 1, 'points_available': 20}]
        self.assertEqual(expected_list, quiz.get_quiz_questions('Sports', 1))


    def test_run_quiz(self):
        pass


    def test_ask_question(self):
        pass


    def test_check_user_answer(self):
        pass


    def test_create_result_record(self):
        pass


    def test_calculate_quiz_results(self):
        pass