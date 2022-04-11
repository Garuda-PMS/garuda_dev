from flask import render_template, redirect, url_for
from app.models.User import User
from app.models.LoginCredential import LoginCredential
from flask_login import current_user
from app.forms.RegistrationForm import RegistrationForm
from app import db

def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.firstname.data, last_name=form.lastname.data)
        db.session.add(user)
        db.session.commit()
        login_credential = LoginCredential(user_id=user.id, user_name=form.username.data)
        login_credential.set_password(form.password.data)
        db.session.add(login_credential)
        db.session.commit()
        return redirect(url_for('login_blueprint.login'))
    return render_template('register.html', form=form)