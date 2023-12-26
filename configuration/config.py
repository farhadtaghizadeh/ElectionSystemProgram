from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
db = SQLAlchemy()
load_dotenv()
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_dbname = os.getenv("DB_NAME")
db_driver = os.getenv("DB_DRIVER")
connection_string = db_driver + db_username + ":" + db_password + "@" + db_host + "/" + db_dbname
engine = db.create_engine(connection_string)
metadata = db.MetaData()