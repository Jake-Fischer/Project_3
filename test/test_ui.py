import ui
import unittest

class TestUI(unittest.TestCase):

    # Struggling to understand how to write tests for things
    # I am wondering if the structure of my program is not test friendly and thats whats causing me issues

    def test_get_user_answer(self):
        self.assertEqual('Word', ui.get_user_answer('Word'))
        self.assertEqual('  ', ui.get_user_answer('  '))
        self.assertEqual('\n', ui.get_user_answer('\n'))
        self.assertEqual('\t', ui.get_user_answer('\t'))


    def test_display_topics_and_number_of_questions(self):
        pass


    def test_request_valid_topic(self):
        pass


    def test_request_number_of_questions(self):
        pass


    def test_ask_question(self):
        pass


    def test_display_quiz_results(self):
        pass