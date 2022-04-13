from app.models.Objective import Objective
from sqlalchemy import ForeignKey
from app import db

class Story(Objective):
    __tablename__ = 'story'
    epic_id = db.Column(db.Integer, ForeignKey('epic.id'))
    #associated_tasks = db.relationship('Task', backref='story', lazy=True)
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'epic_id': self.epic_id
        }