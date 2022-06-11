from sqlalchemy import Table
from engine import engine
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))

user = Table('user', User.metadata)

def create_user_table():
    User.metadata.create_all(bind = engine)

def add_user(username, password):
    hashed_password = generate_password_hash(password, method='sha256')
    new = user.insert().values(username=username, password=hashed_password)
    conn = engine.connect()
    conn.execute(new)
    conn.close()

def del_user(username):
    delete = user.delete().where(user.c.username == username)
    conn = engine.connect()
    conn.execute(delete)
    conn.close()

class Database:
    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password

    def start(self) -> None:
        create_user_table()
        del_user(username = self.user)
        add_user(username = self.user, password = self.password)
