from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import Objective
from app.models import User
from app.models import LoginCredential
from app.models import Epic
from app.models import Story
from app.models import Task

from routes.UserRoute import user_blueprint
from routes.LoginRoute import login_blueprint
from routes.EpicRoute import epic_blueprint
from routes.StoryRoute import story_blueprint
from routes.TaskRoute import task_blueprint

app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(login_blueprint, url_prefix='/login')
app.register_blueprint(epic_blueprint, url_prefix='/epic')
app.register_blueprint(story_blueprint, url_prefix='/story')
app.register_blueprint(task_blueprint, url_prefix='/task')

@app.route('/')
def index():
    return render_template('kanban.html')