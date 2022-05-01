from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from app.models.User import User

'''
Required data for adding a new user - first name, last name, username, password
'''
class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname  = StringField('Last Name', validators=[DataRequired()])
    username  = StringField('Username', validators=[DataRequired()])
    password  = PasswordField('Password', validators=[DataRequired()])
    submit    = SubmitField('Register')

    # Checks if the user already exists
    def validate_username(self, username):
        user = User.query.filter(User.login.has(user_name=username.data)).first()
        if user is not None:
            raise ValidationError('Please use a different username.')