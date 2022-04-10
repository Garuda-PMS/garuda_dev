from models.User import User
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Login(db.Model):
    __tablename__ = 'login_credential'    
    user_id = db.Column(db.Integer, ForeignKey(User.id), primary_key=True)
    user_name = db.Column(db.String(30))
    password = db.Column(db.String(30))
    
    @property
    def serialize(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'password': self.password
        }