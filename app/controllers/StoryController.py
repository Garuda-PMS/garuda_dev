import sys
from flask import render_template, redirect, url_for, request, abort
from app.models.Story import Story
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Controller: Singleton Pattern with __new__ method for fetching single instance
class StoryController:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(StoryController, cls).__new__(cls)
        return cls.instance


    def view(self, story_id):
        pass
    def create(self):
        if request.method != "POST": return
        json_params = request.get_json(True)
        new_story = Story(**json_params)
        db.session.add(new_story)
        db.session.commit()
        return json_params

    def edit(self, epic_id):
        pass