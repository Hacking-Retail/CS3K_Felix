import sqlite3
import pandas as pd

from config import DB_FILE, CSV_FILE, SQL_FILE

# get sql script
with open(SQL_FILE, 'r') as file:
    sql = file.read()

db = sqlite3.connect(DB_FILE)
cursor = db.cursor()

# create table
cursor.executescript(sql)
db.commit()

# insert data
data = pd.read_csv(CSV_FILE)
data.to_sql("cars", db, if_exists='append', index=False)

db.close()
