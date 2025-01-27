def cube(x):
    return x*x*x

print(cube(2))
l = [1,2,4,7,8]
newl = list(map(cube, l))
print(newl)

#filter
def abc(a):
    return a> 4

nnewl = list(filter(abc, l))
print(nnewl)

def gef(g):
    return g<6

nnnewl = list(filter(gef, l))
print(nnnewl)

#Reduce Function
from functools import reduce

number= [1,2,3,4,5,6]
def mysum(x,y):
    return x+y

sum = reduce(mysum, number)
print(sum)

#is vs ==
#is exact location of memory and == covers the values 
