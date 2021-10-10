import quiz
import unittest


class TestQuiz(unittest.TestCase):

    
    def test_get_topics_and_number_of_questions(self):
        expected_dictionary = {'animals':2, 'sports':2, 'literature':1}
        wrong_dictionary = {'notanimals':2, 'notsports':2, 'notliterature':1}
        self.assertEqual(expected_dictionary, quiz.get_topics_and_number_of_questions())
        self.assertNotEqual(wrong_dictionary, quiz.get_topics_and_number_of_questions())


    def test_get_quiz_questions(self):
        expected_list = [{'id': 2, 'category': 'sports', 'question_text': 'How many rings are on the Olympic flag?', 'correct_answer': '5', 'wrong_answer1': 'None', 'wrong_answer2': '4', 'wrong_answer3': '7', 'difficulty': 1, 'points_available': 20}]
        self.assertEqual(expected_list, quiz.get_quiz_questions('sports', 1))
        self.assertFalse(quiz.get_quiz_questions('notsports', 1000))
        self.assertFalse(quiz.get_quiz_questions(None, None))


    def test_run_quiz(self):
        empty_list = []
        example_questions = [{'id': 2, 'category': 'sports', 'question_text': 'How many rings are on the Olympic flag?', 'correct_answer': '5', 'wrong_answer1': 'None', 'wrong_answer2': '4', 'wrong_answer3': '7', 'difficulty': 1, 'points_available': 20}]
        self.assertTrue(quiz.run_quiz(example_questions))
        self.assertFalse(quiz.run_quiz(empty_list))
        

    def test_ask_question(self):
        test_question = {'id': 2, 'category': 'sports', 'question_text': 'How many rings are on the Olympic flag?', 'correct_answer': '5', 'wrong_answer1': 'None', 'wrong_answer2': '4', 'wrong_answer3': '7', 'difficulty': 1, 'points_available': 20}
        test_uid = 'baac6459-f8d9-4bc1-8867-7b6f8a11ca9f'
        empty_dictionary = {}
        empty_string = ''
        self.assertTrue(quiz.ask_question(test_question, test_uid))
        self.assertFalse(quiz.ask_question(empty_dictionary, empty_string))
        

    def test_check_user_answer(self):
        self.assertTrue(quiz.check_user_answer('answer', 'Answer'))
        self.assertTrue(quiz.check_user_answer('\n', '\n'))
        self.assertTrue(quiz.check_user_answer('\t', '\t'))
        self.assertTrue(quiz.check_user_answer('', ''))
        self.assertTrue(quiz.check_user_answer(' ', ' '))
        self.assertIsNone(quiz.check_user_answer(None, None))


    def test_create_result_record(self): # Unsure how to write a unittest for this
        pass


    def test_calculate_quiz_results(self):
        example_uid = '76c775bb-fdc0-4e41-b0c8-ca6e554c5556'
        example_time = '0:00:00.834767'
        empyty_string = ''
        self.assertTrue(quiz.calculate_quiz_results(example_uid, example_time))
        self.assertFalse(quiz.calculate_quiz_results(empyty_string, empyty_string))
