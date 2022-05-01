from flask import Blueprint
from app.controllers.RegisterController import RegisterController

# Mappings between API endpoint and controller functionality using dedicated 'Blueprints'

registerController = RegisterController()
register_blueprint = Blueprint('register_blueprint', __name__)

register_blueprint.route('/', methods=['GET', 'POST'])(registerController.register)