from flask import Blueprint
from app.controllers.EpicController import EpicController

epicController = EpicController()
epic_blueprint = Blueprint('epic_blueprint', __name__)

epic_blueprint.route('/view/<int:epic_id>', methods=['GET'])(epicController.view)
epic_blueprint.route('/create', methods=['POST'])(epicController.create)
epic_blueprint.route('/edit/<int:epic_id>', methods=['PUT'])(epicController.edit)