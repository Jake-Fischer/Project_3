import ui
import unittest

class TestUI(unittest.TestCase):


    def test_display_topics_and_number_of_questions(self):
        pass


    def test_request_valid_topic(self):
        pass


    def test_request_number_of_questions(self):
        pass


    def test_display_question(self):
        pass


    def test_display_quiz_results(self):
        pass


    def test_get_user_answer(self):
        self.assertEqual('Word', ui.get_user_answer('Word'))
        self.assertEqual('  ', ui.get_user_answer('  '))
        self.assertEqual('\n', ui.get_user_answer('\n'))
        self.assertEqual('\t', ui.get_user_answer('\t'))