def calGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

    #calGmean(a,b)

def isGreater(a,b):
    if(a>b):
        print("First Number is greater")
    else:
        print("Second number is greater or equal")
a=9
b= 8
isGreater(a,b)
calGmean(a,b)

def average(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print("Average is :", sum / len(num))

average(5,6,7,8,9)