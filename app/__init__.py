from flask import Flask
from config import Config
from flask_login import LoginManager
from app.models import db, User
from flask_migrate import Migrate
# from flask_fontawesome import FontAwesome



app = Flask(__name__)
app.config.from_object(Config)
# fa = FontAwesome(app)

login_manager = LoginManager()

login_manager.init_app(app)
db.init_app(app)
migrate = Migrate(app, db)

#login manager messages and config
login_manager.login_view ='auth.login'
login_manager.login_message = "You must be logged in to access this page ! "
login_manager.login_message_category = "danger"


#import my blueprint onto the app
from app.blueprints.auth import auth
from app.blueprints.main import main
from app.blueprints.admin import admin

# register the bluepring on the app
app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(admin)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

