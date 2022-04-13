from flask import Blueprint
from app.controllers.LoginController import LoginController

loginController = LoginController()
login_blueprint = Blueprint('login_blueprint', __name__)

login_blueprint.route('/prompt', methods=['GET'])(loginController.prompt_login)
login_blueprint.route('/', methods=['GET', 'POST'])(loginController.login)