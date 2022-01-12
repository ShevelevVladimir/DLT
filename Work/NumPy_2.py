import numpy as np
X = np.arange(0,101)
print(X)
Y = X[X % 2 != 0]
print(Y)
Z = np.arange(0, 101, 1) 
Z[Z%2==1] = -1     
print(Z)
