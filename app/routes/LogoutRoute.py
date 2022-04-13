from flask import Blueprint
from app.controllers.LoginController import LoginController

loginController = LoginController()
logout_blueprint = Blueprint('logout_blueprint', __name__)

logout_blueprint.route('/', methods=['GET'])(loginController.logout)