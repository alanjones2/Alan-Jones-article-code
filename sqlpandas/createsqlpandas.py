import pandas as pd
import sqlite3 as sql

# create df

# download the source data and save it as original_elections.csv
#election_df = pd.read_csv("https://researchbriefings.files.parliament.uk/documents/CBP-8749/HoC-GE2019-results-by-constituency-csv.csv")
#election_df.to_csv('original_elections.csv')

election_df = pd.read_csv('original_elections.csv')

election_df.drop(columns=election_df.columns[0], axis=1, inplace=True)
print(election_df.head())
election_df.drop([
                  'constituency_name', 
                  'mp_firstname',
                  'mp_surname',
                  'ons_region_id',
                  'county_name',
                  'region_name',
                  'country_name',
                  'constituency_type',
                  'declaration_time',
                  'mp_gender'
                  ], axis=1, inplace=True)

# Change case of party names in first_party and secon_party columns
# to be consistent with the party column names
election_df['first_party']=election_df['first_party'].str.lower()
election_df['second_party']=election_df['second_party'].str.lower()

# delete old files
import os
os.system("del elections.db")
os.system("del elections.csv")

#creat new ones

# create db
conn = sql.connect('elections.db')
election_df.to_sql('elections', conn)

# create new version of df
election_df.to_csv('elections.csv', index=False)
