

print(' **********************')
print(' Assignment 4-6 ')
print(' **********************','\n')

import math
a =int(input("Enter the first Number : "))
b =int(input("Enter the second Number : "))

k1=[]
for i in range(1,a+1):
    if a%i==0:
        k1.append(i)

k2=[]
for j in range(1,b+1):
    if b%j==0:
        k2.append(j)

k3=[]
for i in k1:
    for j in k2:
        if i==j:
            k3.append(i)

print('gcd {},{} is : {}'.format(a,b,max(k3)))

icm=((a*b))/max(k3)


print('icm {},{} is : {}'.format(a,b,icm))
