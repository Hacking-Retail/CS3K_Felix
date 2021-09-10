import os

APP_NAME = "Castor3000"
SECRET_KEY = ")_)j5265kj-cu=r#d3%g@jzi7i#nsmb$fgbf@%qs!yrw5=_gkd"

# Directory & Files #
basedir = os.path.abspath(os.path.dirname(__file__))

SQL_FILE = os.path.join(basedir, "sql\cs3k.sql")
CSV_FILE = os.path.join(basedir, "data\Dataset-Hackathon.csv")
DB_FILE = os.path.join(basedir, "data\db_cars.db")

# Database #
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DB_FILE)
SQLALCHEMY_TRACK_MODIFICATIONS = False