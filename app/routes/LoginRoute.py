from flask import Blueprint
from app.controllers.LoginController import LoginController

# Mappings between API endpoint and controller functionality using dedicated 'Blueprints'

loginController = LoginController()
login_blueprint = Blueprint('login_blueprint', __name__)

login_blueprint.route('/prompt', methods=['GET'])(loginController.prompt_login)
login_blueprint.route('/', methods=['GET', 'POST'])(loginController.login)