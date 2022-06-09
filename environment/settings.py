import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

APP_HOST = os.environ.get("HOST")
APP_CONN = os.environ.get("CONN")
# APP_PORT = int(os.environ.get("PORT"))
# APP_DEBUG = bool(os.environ.get("DEBUG"))
# APP_ENV = os.environ.get("ENV")