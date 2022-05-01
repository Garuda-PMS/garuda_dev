from flask import render_template, redirect, url_for
from app.models.User import User
from app.models.LoginCredential import LoginCredential
from flask_login import current_user
from app.forms.RegistrationForm import RegistrationForm
from app import db

# Controller: Singleton Pattern with __new__ method for fetching single instance
class RegisterController:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RegisterController, cls).__new__(cls)
        return cls.instance

    def register(self):
        # if the user is already logged in then we redirect them to the home page
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        # Registration form
        form = RegistrationForm()
        # If the form data is valid
        if form.validate_on_submit():
            # fetch the new user details
            user = User(first_name=form.firstname.data, last_name=form.lastname.data)
            # Create user
            db.session.add(user)
            db.session.commit()
            # Add login credentials to DB
            login_credential = LoginCredential(user_id=user.id, user_name=form.username.data)
            login_credential.set_password(form.password.data)
            db.session.add(login_credential)
            db.session.commit()
            return redirect(url_for('login_blueprint.login'))
        return render_template('register.html', form=form)