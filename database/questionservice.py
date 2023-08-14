from database.models import Question
from database import db
# функция добавление вопроса
# вывести 20 вопросов (фильтр по level)
# проверка ответа
def add_question(main_text, level,correct_answer, variant_1, variant_2, variant_3=None, variant_4=None):
    new_question = Question(main_text=main_text, level=level, correct_answer=correct_answer, variant_1=variant_1,
                            variant_2=variant_2, variant_3=variant_3, variant_4=variant_4)
    db.session.add(new_question)
    db.session.commit()
    return True
def get_questions(level):
    all_questions = Question.query.filter_by(level=level).all()
    return all_questions[:21]
def check_answer(question_id, user_answer):
    question = Question.query.filter_by(question_id=question_id).first()
    if user_answer == question.correct_answer:
        return True
    else:
        return False
