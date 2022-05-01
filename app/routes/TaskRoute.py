from flask import Blueprint
from app.controllers.TaskController import TaskController

# Mappings between API endpoint and controller functionality using dedicated 'Blueprints'

taskController = TaskController()
task_blueprint = Blueprint('task_blueprint', __name__)

task_blueprint.route('/view/<int:task_id>', methods=['GET'])(taskController.view)
task_blueprint.route('/create', methods=['POST'])(taskController.create)
task_blueprint.route('/edit/<int:task_id>', methods=['PUT'])(taskController.edit)