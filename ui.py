from model import Questions, Results
import random

# Creates a dictionary consisting of each topic, and how many questions are attributed to it.
def get_topics_and_number_of_questions():
    questions = Questions.select()
    categories_and_questions = {}
    for question in questions:
        if question.category in categories_and_questions:
            categories_and_questions[question.category] = categories_and_questions[question.category] + 1
        else:
            categories_and_questions[question.category] = 1
    return categories_and_questions

def display_topics_and_number_of_questions(topics_and_number_of_questions):
    print('Here are the topics you can choose from:\n')
    for category in topics_and_number_of_questions:
        print(category + ' which has ' + str(topics_and_number_of_questions[category]) + ' questions in it')
    print('\n')

def request_valid_topic():
    topics_and_number_of_questions = get_topics_and_number_of_questions()
    while True:
        user_topic = input('Please enter your topic of choice:\n')
        if user_topic in topics_and_number_of_questions:
            return user_topic
        else:
            print('Sorry, that is not a valid topic, please try again:\n')

def request_number_of_questions( user_topic ):
    topics_and_number_of_questions = get_topics_and_number_of_questions()
    while True:
        user_number_of_questions = int(input('Please enter the number of questions you would like to be asked:\n'))
        if user_number_of_questions <= topics_and_number_of_questions[user_topic]:
            return user_number_of_questions
        else:
            print('Sorry, that is not a valid number of questions:\n')

def ask_question(question):
    print(f'The category is: {question.category}. The difficulty is {question.difficulty} (1-5 Scale). It is worth {question.points_available} points.\n')
    print(question.question_text)
    possible_answers = [question.correct_answer, question.wrong_answer1, question.wrong_answer2, question.wrong_answer3]
    random.shuffle(possible_answers)
    for a in possible_answers:
        print(f'-{a}')

def get_user_answer():
    user_answer = input('Answer: ')
    return user_answer