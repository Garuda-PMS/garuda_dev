from flask import Blueprint
from app.controllers.UserController import index, store, show, update, delete

user_blueprint = Blueprint('user_blueprint', __name__)

user_blueprint.route('/', methods=['GET'])(index)
user_blueprint.route('/create', methods=['POST'])(store)
user_blueprint.route('/<int:user_id>', methods=['GET'])(show)
user_blueprint.route('/<int:user_id>/edit', methods=['POST'])(update)
user_blueprint.route('/<int:user_id>', methods=['DELETE'])(delete)