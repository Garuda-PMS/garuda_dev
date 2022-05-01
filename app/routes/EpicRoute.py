from flask import Blueprint
from app.controllers.EpicController import EpicController

# Mappings between API endpoint and controller functionality using dedicated 'Blueprints'

epicController = EpicController()
epic_blueprint = Blueprint('epic_blueprint', __name__)

epic_blueprint.route('/view/<int:epic_id>', methods=['GET'])(epicController.view)
epic_blueprint.route('/create', methods=['POST'])(epicController.create)
epic_blueprint.route('/edit/<int:epic_id>', methods=['PUT'])(epicController.edit)