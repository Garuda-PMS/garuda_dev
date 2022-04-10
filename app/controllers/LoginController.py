import sys
from app.models.LoginCredential import LoginCredential
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, redirect, url_for, request, abort

db = SQLAlchemy()
def prompt_login():
    return render_template('kanban.html')
def register():
    pass
def login():
    pass