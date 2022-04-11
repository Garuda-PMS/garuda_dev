from flask import Blueprint
from app.controllers.LoginController import prompt_login, register, login

login_blueprint = Blueprint('login_blueprint', __name__)

login_blueprint.route('/prompt', methods=['GET'])(prompt_login)
login_blueprint.route('/', methods=['GET', 'POST'])(login)
login_blueprint.route('/register', methods=['POST'])(register)