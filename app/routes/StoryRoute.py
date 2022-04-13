from flask import Blueprint
from app.controllers.StoryController import StoryController

storyController = StoryController()
story_blueprint = Blueprint('story_blueprint', __name__)

story_blueprint.route('/create', methods=['POST'])(storyController.create)
story_blueprint.route('/view/<int:story_id>', methods=['GET'])(storyController.view)
story_blueprint.route('/edit/<int:story_id>', methods=['PUT'])(storyController.edit)