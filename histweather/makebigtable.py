import pandas as pd
import glob

fileList = glob.glob('*yearly.csv')

dflist = [ pd.read_csv(df) for df in fileList]

#print(dflist)

bigTable = pd.concat(dflist)

bigTable['Year']=bigTable['Year'].astype('int64')
print(bigTable.columns)

bigTable=bigTable.set_index('Year')
bigTable=bigTable.drop(['Unnamed: 0'],axis=1)
print(bigTable.columns)
bigTable.to_csv('bigtable.csv')