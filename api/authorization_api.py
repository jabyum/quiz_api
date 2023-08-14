from api import api_bp
from database import register_user_db
#url для прохождения регистрации
@api_bp.route("/register/<string:name>/<string:number>", method=["POST"])
def registration_api(name: str, number: str):
    result = register_user_db(name,number)
    return {"status":1, "user_id": result}

