from database.models import Leaders, UserAnswer
from database import db

# запись результата текущего теста
def user_end_test_db(user_id, correct_answers, level):
    exact_user_score = Leaders.query.filter_by(user_id=user_id, level=level).first()
    # Проверка бд
    if exact_user_score:
        exact_user_score.score += correct_answers
        db.session.commit()
    else:
        new_leader_data = Leaders(user_id=user_id, level=level, score=correct_answers)
        db.session.add(new_leader_data)
        db.session.commit()
    return True
# Вывод лидеров из конкретных уровней
def get_top_5_leaders_db(level):
    if level == 0:
        exact_level_leaders = Leaders.query.order_by(Leaders.score.desc()).all
    else:
        exact_level_leaders = Leaders.query.filter_by(level=level).order_by(Leaders.score.desc()).all
    return exact_level_leaders[:6]
def add_user_answer_db(user_id, q_id, user_answer, correctness):
    new_answer = UserAnswer(question_id=q_id, user_answer=user_answer, user_id=user_id, correctness=correctness)
    db.session.add(new_answer)
    db.session.commit()
    return True
