import pandas as pd
cols = [ 'name' , 'gender', 'birth']
years == 2004
pieces = []
df = pd.read_csv('yob2004.csv', sep = ',', engine = 'python' , names = cols)
df['years'] = i
pieces.append(df)
data = pd.concat(pieces, ignore_index = True)
count=df["gender"].value_counts()
