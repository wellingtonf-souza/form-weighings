from dash import Dash
import secrets
from environment import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOSTNAME, MYSQL_PORT, MYSQL_DATABASE
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

URI = "mysql+pymysql://{user}:{password}@{hostname}:{port}/{database}".format(
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        hostname = MYSQL_HOSTNAME,
        port = MYSQL_PORT,
        database = MYSQL_DATABASE
)

server.config.update(
    SECRET_KEY=secrets.token_hex(),
    SQLALCHEMY_DATABASE_URI = URI,
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