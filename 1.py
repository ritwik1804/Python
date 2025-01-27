#Python is platform independent language
print("hello world")
#module are two type built in modules and external modules
print(17*13)
print("hello i am RM \n i am a boy")
'''
hiii
'''
#escape sequence character
print("Hii i am \"Ritwik\" \n")
print("Hey", 6, 7, sep = "~", end = "009\n")
print("harry")
#seperator use  to join lines
#containers are stored in ram
a=1
b= "Ritwik"
c = False
d= complex(8,2)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#list ordered collection of different data types
#tuples are immutable but list are mutable
#in python everything is an object

#Typecasting
#if a number is put in "" then it is a stirng
# ex a="1"
# b="2" print(a+b)
# the conversition of one data type to another data type is typecasting
# two types of typecasting
# expicit and implicit
# explicit means programmer/ developer is doing the conversion
# implicit means the pythom or complier is doing the conversion

#Taking Input from the python
#a= input("Enter your number")
#b= input("Enter number")
#print(int(a)+int(b))
#print(int(a)-int(b))
#print(int(a)*int(b))
#print(float(a)/float(b))

#strings 
#if anyting is double quote or single quote then it is strings

#name = "Ritwik"
#friend = "Hari"
#print("Hello I am " + name + " and He is my friend, "+ friend)
#for character in name:
#    print(name)

#string slicing
#for slicing we only use [] brackets
name = "Ritwik,Mohanty"
print(name[0:8])
len1 = len(name)
print(" Ritwik Mohanty is a ", len1, "letter word")

names="Ritwik"
print(names[-4:-2])#length is 6 so 6-4 =2 but it takes length for negative slicing so it does not take 4th index

#string methods are immutable
#upper()
a="Harry"
print(a.upper())

#lower()
print(a.lower())

#rstrip()
print(a.rstrip("@"))

#replace()
print(a.replace("Harry", "Ritwik"))

#split()
print(a.split(" "))

#capitalize()
print(a.capitalize())

#centre
str1 = "hii i am RM"
print(len(str1))
print(len(str1.center(10)))

#count()
print(a.count("a"))

#endswith()
print(str1.endswith("RM"))

#find()
print(str1.find("i"))

#index()
#print(a.index("hii"))

#isalnum()
print(str1. isalnum())

#isalpha()
print(str1.isalpha())

#islower()
print(str1.islower())

#isprintable()
print(str1.isprintable())

#isspace()
print(str1.isspace())

#istitle()
print(str1.istitle())

#isupper()
print(str1.isupper())

#startswith()
print(str1.startswith("hii"))

#swapcase()
print(str1.swapcase())

#title()
print(str1.title())


