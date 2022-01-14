import numpy as np
import pandas as pd
columnns=["Movie ID","Titles","Gengers"]
df=pd.read_csv('untitled.csv',engine = 'python',names=columnns, delimiter='::')
df
