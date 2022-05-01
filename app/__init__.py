import json
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager, login_required

# Define flask app
app = Flask(__name__)
# Load the config (Database config)
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

# Register the routes
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(login_blueprint, url_prefix='/login')
app.register_blueprint(logout_blueprint, url_prefix='/logout')
app.register_blueprint(objective_blueprint, url_prefix='/objective')
app.register_blueprint(epic_blueprint, url_prefix='/epic')
app.register_blueprint(story_blueprint, url_prefix='/story')
app.register_blueprint(task_blueprint, url_prefix='/task')
app.register_blueprint(register_blueprint, url_prefix='/register')

# Route to access the home page
@app.route('/')
# Login is required to access the home page
@login_required
def index():
    # Render the tasks, epics and stories
    tasks = db.session.query(Task.Task).paginate()
    epics = db.session.query(Epic.Epic).paginate()
    stories = db.session.query(Story.Story).paginate()
    epic_details = [ {'title': epic.title, 'status': epic.status, 'description': epic.description} for epic in epics.items]
    story_details = [ {'title': story.title, 'status': story.status, 'description': story.description} for story in stories.items]
    task_details = [ {'title': task.title, 'status': task.status, 'description': task.description, 'deadline': task.deadline, 'assignee_id': task.assignee_id} for task in tasks.items]
    return render_template('kanban.html', task_details=task_details, epic_details=epic_details, story_details=story_details)

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