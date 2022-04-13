import sys
from flask import render_template, redirect, url_for, request, abort
from app.models.Epic import Epic
from flask_sqlalchemy import SQLAlchemy
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
        pass

    def edit(self, epic_id):
        pass