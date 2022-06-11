from dash import Dash
import secrets
from environment import APP_CONN
from users import db, User as base
from flask_login import LoginManager, UserMixin
import dash_bootstrap_components as dbc
from flask import Flask

server = Flask(__name__)
app = Dash(
    __name__, 
    server = server,
    suppress_callback_exceptions = True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

server.config.update(
    SECRET_KEY=secrets.token_hex(),
    SQLALCHEMY_DATABASE_URI = APP_CONN,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db.init_app(server)

login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/'

class User(UserMixin, base):
    pass

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))