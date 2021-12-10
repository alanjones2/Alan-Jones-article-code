import pandas as pd
import sqlite3 as sql

# create df
election_df = pd.read_csv("https://researchbriefings.files.parliament.uk/documents/CBP-8749/HoC-GE2019-results-by-constituency-csv.csv")

print (election_df)

# create db
conn = sql.connect('elections.db')
election_df.to_sql('elections', conn)

election_df.to_csv('elections.csv')