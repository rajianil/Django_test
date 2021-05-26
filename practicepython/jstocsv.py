import pandas as pd
from pandas import json_normalize
import json
df = pd.read_json(r'C:\Users\Shashi Kumar\PycharmProjects\pythonProject\practicepython\etest.json')
print(df)
#df.to_csv (r'C:\Users\Shashi Kumar\PycharmProjects\pythonProject\practicepython\file.csv')
#print('done')

with open(r'C:\Users\Shashi Kumar\PycharmProjects\pythonProject\practicepython\nestjfile.json') as f:
    data = json.load(f)
print(data)

df=json_normalize(data)
print(df.columns)
print(list(df.columns))

newcol=[]
for i in df.columns:
    #print(i)
    startpos = i.rfind('.')
    #print(i[startpos+1:])
    newcol.append(i[startpos+1:])
print(type(newcol))
print(newcol)
replacingcolumn=dict(zip(list(df.columns), newcol))
df.rename(columns=replacingcolumn, inplace=True)
df.to_csv(r'C:\Users\Shashi Kumar\PycharmProjects\pythonProject\practicepython\nestedfile.csv')

print('newdict',dict(zip(list(df.columns), newcol)))
print(df)