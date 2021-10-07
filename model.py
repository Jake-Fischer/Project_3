from peewee import *
from database_config import database_path

db = SqliteDatabase(database_path)

class Question(Model):
    # Represents a question in the database
    # question_id = IntegerField(unique=True)
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
        return f'{self.category}, {self.question_text}, {self.correct_answer}, {self.wrong_answer1}, {self.wrong_answer2}, {self.wrong_answer3}, {self.difficulty}, {self.points_available}'

class Result(Model):
    # Represents an answer in the database
    timestamp = IntegerField()
    question = ForeignKeyField(Question, backref='question_id') # question_id =  ForeignKeyField(Question, backref = 'question_id') #I am unsure how to make this a foreign key... When I try what's commented out it crashes with this error 'peewee.InterfaceError: Error binding parameter 0 - probably unsupported type.'
    user_answer = CharField()
    points_earned = IntegerField()
    was_correct = BooleanField()
    unique_id = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.timestamp}: {self.question}, {self.user_answer}, {self.points_earned}, {self.was_correct}, {self.unique_id}'

