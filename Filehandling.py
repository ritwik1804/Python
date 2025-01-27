#File Handling 
#f= open('myfile.txt', 'r')
#print(f)
#text = f.read()
#print(text)

#f.write("Hello World")
#f.close()

#with open('myfile.txt', 'a') as f:
#    f.write(" Hey i am inside with")

#Methods
#readlines()
#i=0
#while True:
#    i = i+1
 ##  if not line:
 #      break
#    m1 = int(line.split(",")[0])
#    m2 = int(line.split(",")[1])
#    m3 = int(line.split(",")[2])
##    print(m1)
#    print(m2)
#    print(m3)
#    print(line)

#writelines
#f= open['myfile.txt', 'w']
#lines = ['line 1\n', 'line 2\n', 'line 3\n']
#f.writelines(lines)
#f.close()

#seek()
#with open('myfile.txt', 'r') as f:
   # print(type(f))

    #f.seek(10)
   # print(f.tell())
    #data = f.read(5)

with open('myfile.txt', 'w') as f:
    f.write("Hello World!")
    f.truncate(12)

with open('myfile.txt', 'r') as f:
    print(f.read())


