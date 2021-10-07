import quiz
import ui
import unittest
from unittest.mock import patch   # for creating fake responses from functions/methods
from model import Question, Result

class TestQuiz(unittest.TestCase):

    # 
    def test_get_topics_and_number_of_questions(self):
        expected_dictionary = {'Animals':2, 'Sports':2, 'Literature':1}
        self.assertEqual(expected_dictionary, quiz.get_topics_and_number_of_questions())

    # see example in class agenda for swapping out DB for Peewee tests

    # Testing 

    @patch('ui.get_user_answer')   # replace ui.get_user_answer with a mock, or fake version
    def test_ask_question_user_answers_correctly(self, mock_get_user_answer):  # note 2nd parameter
        
        # arrange...
        example_question = Question(category='food', question_text='type the word pizza', correct_answer='pizza', wrong_answer1='tacos', wrong_answer2='chips', wrong_answer3='soda', difficulty=1, points_available=1)
        example_question.save() 
        mock_get_user_answer.return_value = 'pizza'  # force the get_user_answer function to return a specific value. When called it will return 'pizza'

        # action...
        quiz.ask_question(example_question)

        # assert...
        # todo check database - has the expected Result data been written? 


    # also another test user gets answer wrong, and are there other scenarios to test?