

print(' **********************')
print(' Assignment 4-5 ')
print(' **********************','\n')

import math
a =int(input("Enter a Number : "))

for i in range(2,a):
    if a%math.factorial(i)==0:
        print('The Number is factorial!')

        break

    else:
        print('The Number is not factorial!')
        break

