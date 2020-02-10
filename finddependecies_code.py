import argparse
import pandas as pd
import json

#import arg data, setting dataframes ,merging and sorting based on orders id
parser = argparse.ArgumentParser()
parser.add_argument('order')
parser.add_argument('dependencies')
parser.add_argument('output')
args = parser.parse_args()
dforder = pd.read_csv(args.order, sep=",", header=0)
dfdependency = pd.read_csv(args.dependencies, sep=",", header=0)
df=pd.merge(dfdependency, dforder, on='id', how='outer')
df = df.sort_values(['id'], ascending=[True])
df['check'] = 0

# recursive function for finding children
def find_children(i):
    df.loc[df['id'] == i, 'check'] = 1
    d = {}
    d["id"] = int(i)
    d["name"] = str(df.loc[df.id == i, 'name'].values[0])
    d["dependencies"] = []
    df_children = dfdependency.loc[dfdependency['id'] == i]
    for index, row in df_children.iterrows():
        founded_child = find_children(row['child_id'])

        d["dependencies"].append(founded_child)

    return (d)

# finding parents and storing them
datastore = []
for item in df['id']:
    if ((df.loc[df['id'] == item, 'check'].values[0]) == 0):
        df.loc[df['id'] == item, 'check'] = 1
        datastore.append(find_children(item))
    #saving as a json file
    with open('output.json', 'w') as f:
        json.dump(datastore, f, indent=5)

