import sys
from flask import render_template, redirect, url_for, request, abort
from app.models.Epic import Epic
from flask_sqlalchemy import SQLAlchemy

from app.models.Task import Task
import random;
db = SQLAlchemy()

# Controller: Singleton Pattern with __new__ method for fetching single instance
class TaskController:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TaskController, cls).__new__(cls)
        return cls.instance
    
    def create(self):
        if request.method != "POST": return
        json_params = request.get_json(True)
        new_task = Task(**json_params)
        db.session.add(new_task)
        db.session.commit()
        return json_params

    def view(self, epic_id):
        return epic_id
    
    def edit(self, epic_id):
        return epic_id