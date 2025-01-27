double  = lambda x: x-2
print(double(5))

cube = lambda x: x*x*x
print(cube(3))

avg = lambda x,y: (x+y)/2
print(avg(3,5))

avgg = lambda x,y,z: (x+y-z)/2
print(avgg(4,5,7))

def avggg(a,b):
    return 5* a(b)
print(avggg(lambda a,b: a*b, 2))