from database import db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    phone_number = db.Column(db.String, unique=True)
# таблица лидеров
class Leaders(db.Model):
    __tablename__ = "leaders"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForignKey("users.id"))
    level = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    # подключение к другой таблице
    user_fk = db.relationship(User)
# таблица вопросов
class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    main_text = db.Column(db.String, nullable=False)
    variant_1 = db.Column(db.String, nullable=False)
    variant_2 = db.Column(db.String, nullable=False)
    variant_3 = db.Column(db.String)
    variant_4 = db.Column(db.String)
    correct_answer = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)
# Таблица ответов пользователей на вопросы
class UserAnswer(db.Model):
    __tablename__ = "user_answers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    user_answer = db.Column(db.Integer, nullable=False)
    correctness = db.Column(db.Boolean, default=False)
    user_fk = db.relationship(User)
    question_fk = db.relationship(Question)


