from sqlalchemy import ForeignKey
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class LoginCredential(db.Model):
    __tablename__ = 'login_credential'    
    user_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    user_name = db.Column(db.String(30))
    password = db.Column(db.Text)
    
    @property
    def serialize(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'password': self.password
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)