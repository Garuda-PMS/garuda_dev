from flask import Blueprint
from controllers.TaskController import view, create, edit

task_blueprint = Blueprint('task_blueprint', __name__)

task_blueprint.route('/view/<int:task_id>', methods=['GET'])(view)
task_blueprint.route('/create', methods=['POST'])(create)
task_blueprint.route('/edit/<int:task_id>', methods=['PUT'])(edit)