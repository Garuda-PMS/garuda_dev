from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.forms.LoginForm import LoginForm
from app.models.User import User


def prompt_login():
    return render_template('kanban.html')
def register():
    pass
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.login.has(user_name=form.username.data)).first()
        if user is None or not user.check_password(form.password.data):
            return render_template('login.html', title='Log In', form=form)
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Log In', form=form)
def logout():
    logout_user()
    form = LoginForm()
    render_template('login.html', title='Log In', form=form)