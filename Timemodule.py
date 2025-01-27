import time


def usingWhile():
    i=0
    while i<400:
        i= i+1
        print(i)

def usingFor():
    for i in range(400):
        print(i)

init = time.time()
usingFor()
print(time.time() - init)
usingWhile()