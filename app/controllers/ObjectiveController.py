import sys
from flask import render_template, redirect, url_for, request, abort
from app.models.Objective import Objective
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Controller: Singleton Pattern with __new__ method for fetching single instance
class ObjectiveController:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ObjectiveController, cls).__new__(cls)
        return cls.instance


    def view(self, objective_id):
        pass

    def create(self):
        if request.method != "POST": return
        json_params = request.get_json(True)
        new_objective = Objective(**json_params)
        db.session.add(new_objective)
        db.session.commit()

    def edit(self, epic_id):
        pass