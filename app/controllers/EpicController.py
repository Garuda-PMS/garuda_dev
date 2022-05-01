import sys
from flask import render_template, redirect, url_for, request, abort
from app.models.Epic import Epic
from flask_sqlalchemy import SQLAlchemy

#Invocation of ORM object
db = SQLAlchemy()

# Controller: Singleton Pattern with __new__ method for fetching single instance
class EpicController:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(EpicController, cls).__new__(cls)
        return cls.instance
    
    def view(self, epic_id):
        pass
    
    def create(self):
        if request.method != "POST": return
        json_params = request.get_json(True)
        new_epic = Epic(**json_params)
        db.session.add(new_epic)
        db.session.commit()
        return json_params

    def edit(self, epic_id):
        pass