from flask import Blueprint
from app.controllers.EpicController import view, create, edit

epic_blueprint = Blueprint('epic_blueprint', __name__)

epic_blueprint.route('/view/<int:epic_id>', methods=['GET'])(view)
epic_blueprint.route('/create', methods=['POST'])(create)
epic_blueprint.route('/edit/<int:epic_id>', methods=['PUT'])(edit)