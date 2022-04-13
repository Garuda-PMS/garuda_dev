from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager, login_required

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = '/login'

from app.models import Objective
from app.models import User
from app.models import LoginCredential
from app.models import Epic
from app.models import Story
from app.models import Task

from app.routes.UserRoute import user_blueprint
from app.routes.LoginRoute import login_blueprint
from app.routes.EpicRoute import epic_blueprint
from app.routes.StoryRoute import story_blueprint
from app.routes.TaskRoute import task_blueprint
from app.routes.LogoutRoute import logout_blueprint
from app.routes.RegisterRoute import register_blueprint
from app.routes.ObjectiveRoute import objective_blueprint

app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(login_blueprint, url_prefix='/login')
app.register_blueprint(logout_blueprint, url_prefix='/logout')
app.register_blueprint(objective_blueprint, url_prefix='/objective')
app.register_blueprint(epic_blueprint, url_prefix='/epic')
app.register_blueprint(story_blueprint, url_prefix='/story')
app.register_blueprint(task_blueprint, url_prefix='/task')
app.register_blueprint(register_blueprint, url_prefix='/register')

@app.route('/')
@login_required
def index():
    return render_template('kanban.html')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-store"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "-1"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r