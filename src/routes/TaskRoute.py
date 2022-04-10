from flask import Blueprint
from controllers.TaskController import view, create, edit

task_blueprint = Blueprint('task_blueprint', __name__)

task_blueprint.route('/task/view/<int:task_id>', methods=['GET'])(view)
task_blueprint.route('/task/create', methods=['POST'])(create)
task_blueprint.route('/task/edit/<int:task_id>', methods=['PUT'])(edit)