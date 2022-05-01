from flask import Blueprint
from app.controllers.UserController import UserController

# Mappings between API endpoint and controller functionality using dedicated 'Blueprints'

userController = UserController()
user_blueprint = Blueprint('user_blueprint', __name__)

user_blueprint.route('/', methods=['GET'])(userController.index)
user_blueprint.route('/create', methods=['POST'])(userController.store)
user_blueprint.route('/<int:user_id>', methods=['GET'])(userController.show)
user_blueprint.route('/<int:user_id>', methods=['DELETE'])(userController.delete)
user_blueprint.route('/<int:user_id>/edit', methods=['POST'])(userController.update)