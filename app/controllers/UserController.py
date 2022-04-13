import sys
from flask import render_template, redirect, url_for, request, abort
from app.models.User import User
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Controller: Singleton Pattern with __new__ method for fetching single instance
class UserController:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UserController, cls).__new__(cls)
        return cls.instance

    def index(self):
        pass
    def store(self):
        pass
    def show(self, userId):
        pass
    def update(self, userId):
        pass
    def delete(userId):
        pass