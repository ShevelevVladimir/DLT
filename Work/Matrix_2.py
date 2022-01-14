import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from random import randint
from math import exp
T = 0.8
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
for k in range(501):
    num=np.arange (x)
    rand_1 = num[randint(0,x-1)]
    rand_2 = num[randint(0,x-1)]
    for i in range(x):
        for j in range(x):
            if rand_1 == i:
                if rand_2 == j:
                    matrix [j,i] =matrix [j,i] *(-1)
                    sum_2 = summ(2)
                    trig = sum_2 - sum_1
                    if trig <= 0:
                        matrix_2 == matrix.copy
                        sum_1 == sum_2
                    elif trig > 0:
                        W = exp(-trig/T)
                        P = random.random()
                        while P == 0:
                            P == random.random()
                            if P <= W:
                                matrix_2= matrix.copy
                                sum_1 = sum_2
                            elif P > W:
                                matrix = matrix_2
FinalMatrix = matrix_2
sum_3 = sum_1
print(FinalMatrix)
print(sum_3)
plt.imshow(FinalMatrix)
