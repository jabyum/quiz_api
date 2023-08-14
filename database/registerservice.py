from database.models import User
from database import db
# функция регистрации пользователя
def register_user_db(name, phone_number):
    # проверка пользователя на наличие в бд
    checker = User.query.filter_by(phone_number=phone_number).first()
    if checker:
        return checker.id
    new_user = User(name=name, phone_number=phone_number)
    # добавление в базу
    db.session.add(new_user)
    db.session.commit()
    return new_user.id
