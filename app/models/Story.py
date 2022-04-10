from models.Epic import Epic
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Story(Epic):
    __tablename__ = 'story'
    epic_id = db.Column(db.Integer, ForeignKey(Epic.id))
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'epic_id': self.epic_id
        }