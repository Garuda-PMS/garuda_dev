from flask import Blueprint
from app.controllers.LoginController import LoginController

# Mappings between API endpoint and controller functionality using dedicated 'Blueprints'

loginController = LoginController()
logout_blueprint = Blueprint('logout_blueprint', __name__)

logout_blueprint.route('/', methods=['GET'])(loginController.logout)