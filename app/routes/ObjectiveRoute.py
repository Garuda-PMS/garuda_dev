from flask import Blueprint
from app.controllers.ObjectiveController import ObjectiveController

objectiveController = ObjectiveController()
objective_blueprint = Blueprint('objective_blueprint', __name__)
    
objective_blueprint.route('/view/<int:story_id>', methods=['GET'])(objectiveController.view)
objective_blueprint.route('/create', methods=['POST'])(objectiveController.create)
objective_blueprint.route('/edit/<int:story_id>', methods=['PUT'])(objectiveController.edit)