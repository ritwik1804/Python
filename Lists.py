#Lists
ritwik = [30,20,50,70]
print(ritwik)

print(ritwik[-3])#negative indexing
print(ritwik[-4])
print(ritwik[-1])

if 20 in ritwik:
    print("Yes")
else:
    print("No") 

print(ritwik[1:3:2])
print(ritwik[1:3])

list = [i*i for i in range(10)]
print(list)

#List Methods

#append()
ritwik.append(90)
print(ritwik)

#sort
ritwik.sort()
print(ritwik)

#reverse
ritwik.reverse()
print(ritwik)

#index
ritwik.index(90)
print(ritwik)

#copy
newl =ritwik.copy()
print(ritwik)
print(newl)

#insert
ritwik.insert(1, 55)
print(ritwik)

#extend()
ritwik.extend(newl)
print(ritwik)

#concatenating 2 lists
print(ritwik + newl)