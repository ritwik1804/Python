x= 4 #global  variable
print(x)

def my_function():
    global x
    x=4
    y=5
    print(y)

my_function()
print(x)
#print(y)

#File Handling 
f= open('myfile.txt', 'a')
#print(f)
#text = f.read()
#print(text)

f.write("Hello World")
f.close()

with open('myfile.txt', 'a') as f:
    f.write(" Hey i am inside with")
