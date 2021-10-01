from peewee import *

db = SqliteDatabase('quiz_database.sqlite')

class Questions(Model):
    id = IntegerField()
    category = CharField()
    question_text = CharField()
    correct_answer = CharField()
    wrong_answer1 = CharField()
    wrong_answer2 = CharField()
    wrong_answer3 = CharField()
    difficulty = IntegerField()
    points_available = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.category}, {self.question_text}, {self.correct_answer}, {self.wrong_answer1}, {self.wrong_answer2}, {self.wrong_answer3}, {self.difficulty}, {self.points_available}'


class Results(Model):
    start_time = TimestampField()
    # question_id = # Foreign Key
    user_answer = CharField()
    points_earned = IntegerField()
    was_correct = BooleanField()
    end_time = TimestampField()
    quiz_session = CharField()
    
 #Have python record start and end time and calculate it on its own, not the db

db.connect()

def main():
    categories_and_number_of_questions = get_topics_from_database()
    print(categories_and_number_of_questions)
    display_topics_for_user(categories_and_number_of_questions)
    user_topic_choice = ask_user_for_topic(categories_and_number_of_questions)
    if validate_topic_is_in_dictionary(user_topic_choice, categories_and_number_of_questions):
        ask_user_for_number_of_questions()

# read_topics_from_database
def get_topics_from_database():
    questions = Questions.select()
    categories_and_questions = {}
    for question in questions:
        if question.category in categories_and_questions:
            categories_and_questions[question.category] = categories_and_questions[question.category] + 1
        else:
            categories_and_questions[question.category] = 1
    return categories_and_questions

# display_topics_for_user
def display_topics_for_user(categories_and_questions):
    print('Here are the topics you can choose from')
    for category in categories_and_questions:
        print(category + ' which has ' + str(categories_and_questions[category]) + ' questions in it')

# create_database_table_for_quiz_results

# ask_user_for_topic_and_number_of_questions
def ask_user_for_topic(categories_and_questions):
    user_topic = input('Please enter your topic of choice:\n')
    if validate_topic_is_in_dictionary(user_topic, categories_and_questions):
        return user_topic
    else:
        print('Sorry, that is not a valid topic')

def ask_user_for_number_of_questions(user_topic, categories_and_questions):
    number_of_questions = input('Please enter the number of questions you would like you answer:\n')


def validate_topic_is_in_dictionary(topic, dictionary):
    if topic not in dictionary:
        return False
    else:
        return True

def validate_number_of_questions_in_topic(topic, dictionary, number):
    if number <= dictionary[topic]:
        return True
    else:
        return False

main()
# start_quiz
# record_time_user_started_quiz
# ask_user_questions_one_at_a_time
    # display_question
    # display_topic
    # display_points_available
    # display_difficulty
    # display_four_choices_in_random_order
    # ask_user_for_answer
    # check_answer
    # diaplay_message_and_correct_answer
    # save_entry_in_results_table_with_attempt_identified (What)

# record_time_and_date_of_end_of_quiz
# display_end_of_quiz_message
    # time taken to complete
    # the number of questions asked
    # the number of correct answers
    # the total points available
    # number of points earned
    # percentage score, rounded to two decimal places (=points earned/points available * 100)

# end program