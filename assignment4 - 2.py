

print(' **********************')
print(' Assignment 4-2 ')
print(' **********************','\n')

import math
import numpy as np

a=int(input('Input the a  coefficient in \"ax**2+b*x+c\":  '))
b=int(input('Input the b  coefficient in \"ax**2+b*x+c\":  '))
c=int(input('Input the c  coefficient in \"ax**2+b*x+c\":  '))

if (b**2-4*a*c) >= 0:
    x1 = ((-1 * b) + np.sqrt((b ** 2 - 4 * a * c))) / (2 * a)
    x2 = ((-1 * b) - np.sqrt((b ** 2 - 4 * a * c))) / (2 * a)
    print('x1: {} , x2: {}'.format(x1,x2))

else:
    print('This equation has no answer')

