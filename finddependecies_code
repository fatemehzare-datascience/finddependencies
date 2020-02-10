import pandas as pd
import json

df1 = pd.read_csv('orders.txt', sep=",", header=0)
df2 = pd.read_csv('dependencies.txt', sep=",", header=0)
df2 = df2.sort_values(['id', 'child_id'], ascending=[True, True])
df=pd.merge(df2, df1, on='id', how='outer')
df2['ch']=0


def parent(i):
    d = {}
    d["id"] = i
    d["name"] = str(df.loc[df.id == i, 'name'].values[0])
    d["dependencies"] = []

    a = df2.loc[df2['id'] == i]
    for j in a['child_id']:
        if (row['ch'] == 0):
            b = parent(j)
        d["dependencies"].append(b)
    df2.loc[df2['id'] == i, 'ch'] = 1
    return (d)


g = []
for index, row in df2.iterrows():
    if (row['ch'] == 0):
        g.append(parent(row['id']))
        a = (str(g))
        with open('data.json', 'w') as f:
            json.dump(a, f)
df2.loc[df2['id'] == row['id'], 'ch'] = 1
