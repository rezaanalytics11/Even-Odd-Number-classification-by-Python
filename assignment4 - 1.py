print(' **********************')
print(' Assignment 4-1 ')
print(' **********************','\n')

m = int(input("Enter Number of rows: "))
n =  int(input("Enter Number of columns: "))

c=list([n*'#'])
d=[]
for i in c:
    d.append('*'.join(i))


print('\n'.join(m*d))

