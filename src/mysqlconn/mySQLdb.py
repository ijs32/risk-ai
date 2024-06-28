import dotenv
import os
from sqlalchemy import create_engine

dotenv.load_dotenv('./mysqlconn/.env')

DB_USER = os.getenv('DB_USER')
DB_PASSWD = os.getenv('DB_PASSWD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

def get_engine():
    engine = create_engine(
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWD}@{DB_HOST}/{DB_NAME}")

    return engine
