from app import db
from app.models.Objective import Objective

#Epic: Generic body of work which can be broken down into stories
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