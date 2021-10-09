from peewee import *
from database_config import database_path
from model import Question, Result


"""This program drops all existing tables in a given database and repopulates the question table with default data"""


db = SqliteDatabase(database_path)


db.connect()


Question.drop_table()
Result.drop_table()


def populate_test_data():

    db.create_tables([Question, Result])
    #1
    Question.create(
    category = 'animals',
    question_text = 'What is the longest that an elephant has ever lived? (That we know of)',
    correct_answer = '86 Years',
    wrong_answer1 = '17 Years',
    wrong_answer2 = '49 Years',
    wrong_answer3 = '142 Years',
    difficulty = 3,
    points_available = 60)
    #2
    Question.create(
    category = 'sports',
    question_text = 'How many rings are on the Olympic flag?',
    correct_answer = '5',
    wrong_answer1 = 'None',
    wrong_answer2 = '4',
    wrong_answer3 = '7',
    difficulty = 1,
    points_available = 20)
    #3
    Question.create(
    category = 'animals',
    question_text = 'What is a tarsier?',
    correct_answer = 'A primate',
    wrong_answer1 = 'A lizard',
    wrong_answer2 = 'A bird',
    wrong_answer3 = 'A fish',
    difficulty = 5,
    points_available = 100)
    #4
    Question.create(
    category = 'literature',
    question_text = 'How did Spider-Man get his powers?',
    correct_answer = 'Bitten by a radioactive spider',
    wrong_answer1 = 'Woke up with them after a strange dream',
    wrong_answer2 = 'Born with them',
    wrong_answer3 = 'Military experiment gone awry',
    difficulty = 1,
    points_available = 20)
    #5
    Question.create(
    category = 'sports',
    question_text = 'In darts, what\'s the most points you can score with a single throw?',
    correct_answer = '60',
    wrong_answer1 = '20',
    wrong_answer2 = '50',
    wrong_answer3 = '100',
    difficulty = 3,
    points_available = 60)


populate_test_data()
