from app import db

class Objective(db.Model):
    __abstract__ = True  
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(1000))
    status = db.Column(db.String(20))    
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }