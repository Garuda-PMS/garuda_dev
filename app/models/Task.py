from sqlalchemy import ForeignKey
from app.models.Objective import Objective
from app import db

class Task(Objective):
    __tablename__ = 'task'

    deadline = db.Column(db.Integer)
    assignee_id = db.Column(db.Integer, ForeignKey('user.id'))
    story_id = db.Column(db.Integer, ForeignKey('story.id'))