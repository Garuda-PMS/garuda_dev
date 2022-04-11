from app import db
from app import login
from flask_login import UserMixin

class User(UserMixin, db.Model):
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
    
    def set_password(self, password):
        self.login.set_password(password)

    def check_password(self, password):
        return self.login.check_password(password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))