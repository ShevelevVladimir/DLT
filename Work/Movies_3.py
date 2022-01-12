import numpy as np
import pandas as pd
users = pd.read_csv('users.csv', header=None, engine = 'python',names=["UserID","Gender","Age","Occupation","Zip-code"], delimiter='::')
rating = pd.read_csv('rating.csv', header=None, engine = 'python',names=["UserID","MovieID","Rating","Timestamp"], delimiter='::')
new = pd.merge(rating,users)
df = pd.pivot_table(new, index=["Gender","Age"])
del df["MovieID"]
del df["Occupation"]
del df["Timestamp"]
del df["UserID"]
g2=df.sort_values(by="Rating",ascending=False)
g2
