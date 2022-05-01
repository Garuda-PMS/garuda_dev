import copy
from app import db

# Objective: High-level initiative that must be achieved for goal completion
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
    
    def __repr__(self):
        return ":".join(self.serialize.values())