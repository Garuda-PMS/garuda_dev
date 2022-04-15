from sqlalchemy import ForeignKey
from app.models.Objective import Objective
from app import db

class Task(Objective):
    __tablename__ = 'task'

    deadline = db.Column(db.Integer)
    assignee_id = db.Column(db.Integer, ForeignKey('user.id'))
    #story_id = db.Column(db.Integer, ForeignKey('story.id'))

    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'deadline': self.deadline,
            'assignee_id': self.assignee_id
        }
    