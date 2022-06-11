import os

MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_HOSTNAME = os.environ.get("MYSQL_HOSTNAME")
MYSQL_PORT = os.environ.get("MYSQL_PORT")
APP_HOST = os.environ.get("APP_HOST")
APP_PORT = int(os.environ.get("PORT"))
AWS_REGION_NAME = os.environ.get("AWS_REGION_NAME")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
USER = os.environ.get("APP_USER")
PASSWORD = os.environ.get("APP_PASSWORD")