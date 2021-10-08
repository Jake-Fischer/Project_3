import random


def display_topics_and_number_of_questions(topics_and_number_of_questions):
    """Display a list of topics to the user"""

    print('Here are the topics you can choose from:\n')
    for category in topics_and_number_of_questions:
        print(category + ' which has ' + str(topics_and_number_of_questions[category]) + ' questions in it')
    print('\n')


def request_valid_topic(topics_and_number_of_questions):
    """Ask the user for a valid topic"""

    while True:
        user_topic = input('Please enter your topic of choice:\n')
        if user_topic in topics_and_number_of_questions:
            return user_topic
        else:
            print('Sorry, that is not a valid topic, please try again:\n')


def request_number_of_questions(user_topic, topics_and_number_of_questions):
    """Ask the user for the number of questions they would like"""

    while True:
        user_number_of_questions = int(input('Please enter the number of questions you would like to be asked:\n'))
        if user_number_of_questions <= topics_and_number_of_questions[user_topic]:
            return user_number_of_questions
        else:
            print('Sorry, that is not a valid number of questions:\n')


def display_question(question):
    """Print the question information and answers in random order"""

    category = question['category']
    difficulty = question['difficulty']
    points_available = question['points_available']
    question_text = question['question_text']
    correct_answer = question['correct_answer']
    wrong_answer1 = question['wrong_answer1']
    wrong_answer2 = question['wrong_answer2']
    wrong_answer3 = question['wrong_answer3']
    print(f'The category is: {category}. The difficulty is {difficulty} (1-5 Scale). It is worth {points_available} points.\n')
    print(question_text)
    possible_answers = [correct_answer, wrong_answer1, wrong_answer2, wrong_answer3]
    random.shuffle(possible_answers)
    for a in possible_answers:
        print(f'-{a}')


def display_quiz_results(time_taken, number_of_questions_asked, number_of_questions_correct, total_points_available, total_points_earned, score):
    """Print quiz result data"""

    print('-----Here are the results for your quiz-----\n')
    print(f'It took you {time_taken} hours to complete this quiz.')
    print(f'You got {number_of_questions_correct} out of {number_of_questions_asked} questions correct.')
    print(f'Your score is {total_points_earned}/{total_points_available}, which is a score of {score}%')
    print('Thank you for using this quiz program!\nPlease run the program again to try again.')


def get_user_answer():
    """Obtain user input"""
    
    user_answer =  input('Answer: ')
    return user_answer