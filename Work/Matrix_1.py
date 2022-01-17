import pandas as pd
import numpy as np
import random
from random import randint
rone =[1,-1]
x = int(input("Введите число, превышающее 2: "))
if x<=2:
    x = 0;
if x < 2:
    print("Ошибка! Число меньше 2!");
matrix = np.ones((x,x))
for i in range(x):
    for j in range(x):
        matrix[j,i]=rone[randint(0,1)]
def summ(v):
    summ = 0
    for j in range(x):
        for k in range(x):
            if (j-1)>=-1:
                summ += matrix[j,k] * matrix[j-1,k]
    for j in range(x):
        for k in range(x):
            if (k-1)>=-1:
                summ += matrix[j,k] * matrix[j,k-1]
                if v == 1:
                    sum_1 = summ
                    return(sum_1)
                elif v == 2:
                    sum_2 = summ
                    return(sum_2)
sum_1 = summ(1)
matrix_2 = matrix
print(matrix_2)
