from environment import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOSTNAME, MYSQL_PORT, MYSQL_DATABASE
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://{user}:{password}@{hostname}:{port}/{database}".format(
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        hostname = MYSQL_HOSTNAME,
        port = MYSQL_PORT,
        database = MYSQL_DATABASE
    )
)