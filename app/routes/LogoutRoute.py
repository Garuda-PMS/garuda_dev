from flask import Blueprint
from app.controllers.LoginController import logout

logout_blueprint = Blueprint('logout_blueprint', __name__)

logout_blueprint.route('/', methods=['GET'])(logout)