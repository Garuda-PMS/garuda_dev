from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from app.forms.LoginForm import LoginForm
from app.models.User import User

'''
Handles User login and User logout
'''
class LoginController():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoginController, cls).__new__(cls)
        return cls.instance

    def prompt_login(self):
        return render_template('kanban.html')

    def login(self):
        # If the user is already logged in then the user session is used to recognise this and the 
        # user is redirected to the index page without asking for login a second time
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        # Login form
        form = LoginForm()
        # First we check if the form data provided is valid
        if form.validate_on_submit():
            # Fetch user based on form input
            user = User.query.filter(User.login.has(user_name=form.username.data)).first()
            # Validate user
            if user is None or not user.login.check_password(form.password.data):
                # if user is invalid
                return render_template('login.html', title='Log In', form=form)
            # if user is valid
            login_user(user)
            # This is required in case the user was initially accessing a page that required a login and was hence redirected
            # to the login page
            next_page = request.args.get('next')
            # The default page to be displayed after login
            if not next_page:
                next_page = url_for('index')
            return redirect(next_page)
        
        return render_template('login.html', title='Log In', form=form)

    def logout(self):
        logout_user()
        form = LoginForm()
        render_template('login.html', title='Log In', form=form)