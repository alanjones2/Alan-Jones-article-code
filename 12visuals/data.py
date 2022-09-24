import pandas as pd
import matplotlib.pyplot as plt

url='data/tempbydecade.csv'
gwdec = pd.read_csv(url, delimiter=' ', skipinitialspace=True)
gwdec=gwdec.set_index('Year')
gwdec.to_csv('data/bydecade.csv')