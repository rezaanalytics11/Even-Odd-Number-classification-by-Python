

print(' **********************')
print(' Assignment 4-3 ')
print(' **********************','\n')

import numpy as np


m =int(input("Enter Number of rows: "))
n =int(input("Enter Number of columns: "))

k=[]
for i in range(1,m+1):
    for j in range(1,n+1):
        k.append(i*j)

k=np.array(k).reshape(10,-1)

print(k)

