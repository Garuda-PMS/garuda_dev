from app import db

class User(db.Model):
    __tablename__ = 'user'    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    login = db.relationship('LoginCredential', backref='user', lazy=True, uselist=False)
    assigned_tasks = db.relationship('Task', backref='user', lazy=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }