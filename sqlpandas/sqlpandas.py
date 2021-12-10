import pandas as pd
import sqlite3 as sql

# create df
election_df = pd.read_csv('elections.csv')

# create db
conn = sql.connect('elections.db')

cur = conn.execute("SELECT * FROM elections")
rows = cur.fetchall()
print(rows[0:4])

