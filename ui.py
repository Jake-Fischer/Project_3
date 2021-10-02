import quiz
import random


def display_topics_and_number_of_questions(topics_and_number_of_questions): # Displays a list of topics to the user
    print('Here are the topics you can choose from:\n')
    for category in topics_and_number_of_questions:
        print(category + ' which has ' + str(topics_and_number_of_questions[category]) + ' questions in it')
    print('\n')


def request_valid_topic(): # Asks the user for a valid topic
    topics_and_number_of_questions = quiz.get_topics_and_number_of_questions()
    while True:
        user_topic = input('Please enter your topic of choice:\n')
        if user_topic in topics_and_number_of_questions:
            return user_topic
        else:
            print('Sorry, that is not a valid topic, please try again:\n')


def request_number_of_questions( user_topic ): # Asks the user for the number of questions they would like
    topics_and_number_of_questions = quiz.get_topics_and_number_of_questions()
    while True:
        user_number_of_questions = int(input('Please enter the number of questions you would like to be asked:\n'))
        if user_number_of_questions <= topics_and_number_of_questions[user_topic]:
            return user_number_of_questions
        else:
            print('Sorry, that is not a valid number of questions:\n')


def ask_question(question): # Prints the question information and answers in random order
    print(f'The category is: {question.category}. The difficulty is {question.difficulty} (1-5 Scale). It is worth {question.points_available} points.\n')
    print(question.question_text)
    possible_answers = [question.correct_answer, question.wrong_answer1, question.wrong_answer2, question.wrong_answer3]
    random.shuffle(possible_answers)
    for a in possible_answers:
        print(f'-{a}')


def display_quiz_results(tt, number_of_questions_asked, number_of_questions_correct, total_points_available, total_points_earned, score): # Prints quiz result data
    print('-----Here are the results for your quiz-----\n')
    print(f'It took you {tt} hours to complete this quiz.')
    print(f'You got {number_of_questions_correct} out of {number_of_questions_asked} questions correct.')
    print(f'Your score is {total_points_earned}/{total_points_available}, which is a score of {score}%')
    print('Thank you for using this quiz program!\nPlease run the program again to try again.')


def get_user_answer():
    user_answer =  input('Answer: ')
    return user_answer