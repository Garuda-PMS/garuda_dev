from flask_sqlalchemy import SQLAlchemy
from models.Objective import Objective
db = SQLAlchemy()
class Epic(Objective):
    __tablename__ = 'epic'

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }