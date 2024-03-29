import pandas as pd
import requests
import io

file = io.StringIO(requests.get(url).text)

col_names = ('Year','Month','Tmax','Tmin','AF','Rain','Sun','status')

weather = pd.read_csv(file,
    header=None,
    names=col_names,
    delimiter=' ',
    skipinitialspace=True,
    on_bad_lines = 'skip',
    usecols = col_names)