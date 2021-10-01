import model
import ui
import quiz

def main():
    
    topics_and_questions = quiz.get_topics_and_number_of_questions()

    ui.display_topics_and_number_of_questions(topics_and_questions)

    topic_chosen = ui.request_valid_topic()

    number_of_questions = ui.request_number_of_questions(topic_chosen)
    
    quiz_questions = quiz.get_quiz_questions(topic_chosen, number_of_questions)

    quiz.run_quiz(quiz_questions)

    model.db.close()


if __name__ == '__main__':
    main()