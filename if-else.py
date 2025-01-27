#conditional operator > < >= <= == !=
#a= int(input(""))
#print("Your age is", a)

#if(a>18):
#    print("You can drive")
#else:
#    print("You cannot drive")


#if-elif-else
#num = int(input(""))
#if(num<0):
#    print("Num is negative")
#elif(num == 0):
#    print("Num is zero")
#else:
#    print("Number is positive")


#num = int(input(""))
#if(num < 0):
#   print("Number is Negative")
#elif(num>0):
#    if(num <= 10):
#        print("Num is btw 1-10")
#    elif(num>= 10):
#        print("Number is between 10-20")
#    else:
#        print("Number is greater than 20")
#else:
#    print("Number is 0")



#match case
x= int(input(""))
 
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _ if x != 90:
        print(x," is not used")
    case _ if x != 80:
        print(x," is not 80")
    case _:
        print("x is not")
    

#Short Hand if-else
a= 12
b= 19
print(a) if a>b else print(b) if a== b else print(b)


