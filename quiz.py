from model import Questions, Results
import ui
from datetime import datetime
import time
import uuid

def get_quiz_questions(topic, number_of_questions):
    topic_questions = Questions.select().where(Questions.category == topic)
    quiz_questions = []
    for i in range(number_of_questions):
        question = topic_questions[i]
        quiz_questions.append(question)
    return quiz_questions

def run_quiz(quiz_questions):
    start_time = datetime.now()
    unique_id = uuid.uuid4()
    print('The quiz has begun! Please enter your answers.\n')
    for question in quiz_questions:
        ui.ask_question(question)
        was_correct = False
        user_answer = ui.get_user_answer()
        time_attempted = time.time()
        points_earned = 0
        if check_user_answer(question.correct_answer, user_answer) == True:
            print(f'Correct! The answer was {question.correct_answer}\n')
            was_correct = True
            points_earned = question.points_available
        else:
            print(f'Sorry, that was Incorrect. The correct answer was {question.correct_answer}\n')
        print(f'Time {time_attempted}. Question ID {question.question_id}. User answer {user_answer}. Points earned {points_earned}. Was correct {was_correct}. Unique ID {unique_id}')
        create_result_record(time_attempted, question.question_id, user_answer, points_earned, was_correct, unique_id)
        
def check_user_answer(correct_answer, user_answer):
    if correct_answer == user_answer:
        return True
    else:
        return False

def create_result_record(time_attempted, question_id, user_answer, points_earned, was_correct, unique_id):
    result = Results.create(timestamp=time_attempted, question_id=question_id, user_answer=user_answer, points_earned=points_earned, was_correct=was_correct, unique_id=unique_id)
    result.save()