import copy
from app import db

class Objective(db.Model):
    __abstract__ = True  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(1000))
    status = db.Column(db.String(20))    
    
    #Prototype pattern: DeepCopy module
    def __copy__(self):
        return copy.deepcopy(self)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }