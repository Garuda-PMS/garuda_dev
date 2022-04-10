from app import db
from app.models.Objective import Objective

class Epic(Objective):
    __tablename__ = 'epic'
    associated_stories = db.relationship('Story', backref='epic', lazy=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }