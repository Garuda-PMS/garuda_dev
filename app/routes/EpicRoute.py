from flask import Blueprint
from controllers.EpicController import view, create, edit

epic_blueprint = Blueprint('epic_blueprint', __name__)

epic_blueprint.route('/epic/view/<int:epic_id>', methods=['GET'])(view)
epic_blueprint.route('/epic/create', methods=['POST'])(create)
epic_blueprint.route('/epic/edit/<int:epic_id>', methods=['PUT'])(edit)