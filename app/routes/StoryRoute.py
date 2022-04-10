from flask import Blueprint
from controllers.StoryController import view, create, edit

story_blueprint = Blueprint('story_blueprint', __name__)

story_blueprint.route('/view/<int:story_id>', methods=['GET'])(view)
story_blueprint.route('/create', methods=['POST'])(create)
story_blueprint.route('/edit/<int:story_id>', methods=['PUT'])(edit)