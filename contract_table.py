import pandas as pd
df = pd.read_csv('contract.csv', header=None, engine = 'python', names=["Name","Percent","Growth/Decline","Deadline","Whitepaper"], delimiter='::')
df
