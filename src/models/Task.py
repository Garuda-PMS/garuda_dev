from models.User import User
from models.Story import Story
from sqlalchemy import ForeignKey
from models.Objective import Objective
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Task(Objective):
    __tablename__ = 'task'
    deadline = db.Column(db.Integer)
    assignee_id = db.Column(db.Integer, ForeignKey(User.id))
    reporter_id = db.Column(db.Integer, ForeignKey(User.id))
    story_id = db.Column(db.Integer, ForeignKey(Story.id))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'deadline': self.deadline,
            'assignee_id': self.assignee_id,
            'reporter_id': self.reporter_id,
            'story_id': self.story_id
        }