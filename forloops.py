#FOR LOOPS IN PYTHON
colors = ["Red", "Blue", "Green", "Yellow"]
for x in colors:
    print(colors)

for k in range(5):
    print(k+1)


count = 5
while(count > 5):
    print(count)
    count = count -1
else:
    print("Error")


#break and continue statement
for i in range(12):
    if(i==10):
        continue
    print("5 X", i+1,"=", 5* (i+1))


i =0
while True:
    print(i)
    i=i+1
    if(i%100 == 0):
        break

#for loops with else
for i in range(6):
    print(i)
    if i == 4:
        break #loop is break not finished thats why else will not be printed
else:
    print("Sorry no i")

i=0
while i<7:
    print(i)
    i=i+1

else:
    print("Sorry no i")