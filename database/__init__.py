from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# импорт всех функций (* - всё)
from database.leaderservice import *
from database.questionservice import *
from database.registerservice import *
