from model import Questions, Results
import ui
from datetime import datetime
import time
import uuid


def get_topics_and_number_of_questions(): # Obtain all topics and the number of questions in each. Return in a dictionary.
    questions = Questions.select(Questions.category)
    categories_and_questions = {}
    for question in questions:
        if question.category in categories_and_questions:
            categories_and_questions[question.category] = categories_and_questions[question.category] + 1
        else:
            categories_and_questions[question.category] = 1
    return categories_and_questions


def get_quiz_questions(topic, number_of_questions): # Obtain a specific number of questions from the database from a given topic. Return question data in a list.
    topic_questions = Questions.select(Questions.question_id, Questions.category, Questions.question_text, Questions.correct_answer, Questions.wrong_answer1, Questions.wrong_answer2, Questions.wrong_answer3, Questions.difficulty, Questions.points_available).where(Questions.category == topic)
    quiz_questions = []
    for i in range(number_of_questions):
        question = topic_questions[i]
        quiz_questions.append(question)
    return quiz_questions


def run_quiz(quiz_questions): # Executes a quiz with a given question list
    start_time = datetime.now() 
    unique_id = uuid.uuid4() # Create unique ID that will be assigned to all question results from this quiz

    print('The quiz has begun! Please enter your answers.\n')
    for question in quiz_questions: # Ask the question, initialize default values for the Results table
        ui.ask_question(question)
        was_correct = False
        user_answer = ui.get_user_answer()
        time_attempted = time.time()
        points_earned = 0
        if check_user_answer(question.correct_answer, user_answer): # Check if question is correct
            print(f'Correct! The answer was {question.correct_answer}\n')
            was_correct = True
            points_earned = question.points_available
        else:
            print(f'Sorry, that was Incorrect. The correct answer was {question.correct_answer}\n')
        # Create a record for each question asked
        create_result_record(time_attempted, question.question_id, user_answer, points_earned, was_correct, unique_id)
    # On quiz completion, calculate endtime
    end_time = datetime.now()
    total_time_taken = end_time - start_time
    calculate_quiz_results(unique_id, total_time_taken)
        

def check_user_answer(correct_answer, user_answer):
    if correct_answer == user_answer:
        return True
    else:
        return False


def create_result_record(time_attempted, question_id, user_answer, points_earned, was_correct, unique_id): # Create a record for the question that was answered
    result = Results(timestamp = time_attempted, question_id = question_id, user_answer = user_answer, points_earned = points_earned, was_correct = was_correct, unique_id = unique_id)
    result.save()


def calculate_quiz_results(unique_id, total_time_taken):
    uid = unique_id # Changed for clarity
    tt = total_time_taken # Changed for clarity
    number_of_questions_asked = 0
    number_of_questions_correct = 0
    total_points_available = 0
    total_points_earned = 0
    
    for question_result in Results.select(Results.question_id).where(Results.unique_id == uid): # Select the question_id from all rows where the unique id is the same as the one given to the function
        number_of_questions_asked = number_of_questions_asked + 1 # Add one to question count
        for question in Questions.select(Questions.points_available).where(Questions.question_id == question_result.question_id): # Select the points available feild from Questions rows where Question.question_id is equal to Results.question_id 
            total_points_available = total_points_available + question.points_available # Add to total points available
    
    for question_result in Results.select(Results.points_earned).where(Results.unique_id == uid, Results.was_correct): # Select the points_earned feild from all with the correct unique_id and that were correct
        number_of_questions_correct = number_of_questions_correct + 1 # Add one to the correct count
        total_points_earned = total_points_earned + question_result.points_earned # Add the points earned from the question
        
    score = total_points_earned / total_points_available * 100

    ui.display_quiz_results(tt, number_of_questions_asked, number_of_questions_correct, total_points_available, total_points_earned, score)


