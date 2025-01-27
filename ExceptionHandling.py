#Exception Handling 
a= input("Enter the number")
print(f"Multiplication of table {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input!")

print("Some lines of the code")
print("End of Program")

try:
    num = int(input("Enter number"))
    a =[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")

#Finally Clause
try:
    l=[1,3,5,6]
    i = int(input("Enter number"))
    print(l[i])
except:
    print("Some error produced")

finally:
    print("Hii, I am there")
#it is used to break a database connecion to remove or break from it

#Custom Errors
a = int(input("Enter any value between 5"))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
