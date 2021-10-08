from model import Question, Result
import ui
from datetime import datetime
import time
import uuid


def get_topics_and_number_of_questions():

    """Obtain all topics and the number of questions in each. Return in a dictionary."""
    question_categories = Question.select(Question.category)
    categories_and_question_count = {}
    for question in question_categories:
        if question.category in categories_and_question_count:
            categories_and_question_count[question.category] = categories_and_question_count[question.category] + 1
        else:
            categories_and_question_count[question.category] = 1
    return categories_and_question_count


def get_quiz_questions(topic, number_of_questions):

    """Obtain a specific number of questions from the database from a given topic. Save question data in a dictionary and add it to a list. Return list of question dictionaries."""
    quiz_questions = []
    for question in Question.select(Question.id, Question.category, Question.question_text, Question.correct_answer, Question.wrong_answer1, Question.wrong_answer2, Question.wrong_answer3, Question.difficulty, Question.points_available).where(Question.category == topic).limit(number_of_questions):
            question_data = {}
            question_data['id'] = question.id
            question_data['category'] = question.category
            question_data['question_text'] = question.question_text
            question_data['correct_answer'] = question.correct_answer
            question_data['wrong_answer1'] = question.wrong_answer1
            question_data['wrong_answer2'] = question.wrong_answer2
            question_data['wrong_answer3'] = question.wrong_answer3
            question_data['difficulty'] = question.difficulty
            question_data['points_available'] = question.points_available
            quiz_questions.append(question_data)
    # print(quiz_questions)
    return quiz_questions


def run_quiz(quiz_questions):

    """Executes a quiz"""
    start_time = datetime.now()
    unique_id = uuid.uuid4() # Create unique ID that will be assigned to all question results from this quiz
    print('The quiz has begun! Please enter your answers.\n')
    for question in quiz_questions: # Ask the question, initialize default values for the Results table
        ask_question(question, unique_id)
    end_time = datetime.now()
    total_time_taken = end_time - start_time
    calculate_quiz_results(unique_id, total_time_taken)
        

def ask_question(question, unique_id):

    """Ask the user a question"""
    ui.display_question(question)
    correct_answer = question['correct_answer']
    question_id = question['id']
    was_correct = False
    user_answer = ui.get_user_answer()
    time_attempted = time.time()
    points_earned = 0
    if check_user_answer(correct_answer, user_answer): # Check if question is correct
        print(f'Correct! The answer was {correct_answer}\n')
        was_correct = True
        points_earned = question['points_available']
    else:
        print(f'Sorry, that was Incorrect. The correct answer was {correct_answer}\n')
    create_result_record(time_attempted, question_id, user_answer, points_earned, was_correct, unique_id)


def check_user_answer(correct_answer, user_answer):

    """Check if correct_answer is equal to user_answer"""
    if correct_answer == user_answer:
        return True
    else:
        return False


def create_result_record(time_attempted, question_id, user_answer, points_earned, was_correct, unique_id):

    """Create a record for the question that was answered"""
    result = Result(timestamp = time_attempted, question_id = question_id, user_answer = user_answer, points_earned = points_earned, was_correct = was_correct, unique_id = unique_id)
    result.save()


def calculate_quiz_results(unique_id, total_time_taken):
    
    """Calculate test results and call a function to display them"""
    number_of_questions_asked = Result.select().where(Result.unique_id == unique_id).count()
    number_of_questions_correct = Result.select().where(Result.unique_id == unique_id, Result.was_correct == True).count()
    total_points_available = 0
    total_points_earned = 0

    for result in Result.select(Result.points_earned).where(Result.unique_id == unique_id): # Calculate total points earned
        total_points_earned = total_points_earned + result.points_earned
    
    for question in Question.select(Question.points_available).where(Result.unique_id == unique_id).join(Result): # Calculate total points available
        total_points_available = total_points_available + question.points_available
        
    score = total_points_earned / total_points_available * 100

    ui.display_quiz_results(total_time_taken, number_of_questions_asked, number_of_questions_correct, total_points_available, total_points_earned, score)
