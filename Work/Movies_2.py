import numpy as np
import pandas as pd
rating = pd.read_csv('rating.csv', header=None, engine = 'python',names=["UserID","MovieID","Rating","Timestamp"], delimiter='::')
users = pd.read_csv('users.csv', header=None, engine = 'python',names=["UserID","Gender","Age","Occupation","Zip-code"], delimiter='::')
new = pd.merge(rating,users)
movies = pd.read_csv('untitled.csv',header=None, engine = 'python',names=["MovieID","Titles","Genres"], delimiter='::')
df = pd.merge(new,movies)
df
