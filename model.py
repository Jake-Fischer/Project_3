from peewee import *
from database_config import database_path

db = SqliteDatabase(database_path)

class Question(Model):
    category = CharField()
    question_text = CharField()
    correct_answer = CharField()
    wrong_answer1 = CharField()
    wrong_answer2 = CharField()
    wrong_answer3 = CharField()
    difficulty = IntegerField(constraints = [Check(' 0 > difficulty <= 5')])
    points_available = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.category}, {self.question_text}, {self.correct_answer}, {self.wrong_answer1}, {self.wrong_answer2}, {self.wrong_answer3}, {self.difficulty}, {self.points_available}, {self.id}'

class Result(Model):
    timestamp = IntegerField()
    question = ForeignKeyField(Question, backref='questions')
    user_answer = CharField()
    points_earned = IntegerField()
    was_correct = BooleanField()
    unique_id = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.timestamp}, {self.user_answer}, {self.points_earned}, {self.was_correct}, {self.unique_id}'

