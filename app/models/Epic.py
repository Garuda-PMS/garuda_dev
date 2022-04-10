from app.models.Objective import Objective

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