from flask import Flask
from database import db
app = Flask(__name__)
# настройка базы данных
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///quiz.db"
db.init_app(app)
