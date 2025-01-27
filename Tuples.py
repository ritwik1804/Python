tup = (1,5,6,6)
print(type(tup))
#tuples are immutable and cannot be changed
print(len(tup))
print(tup[-1])
print(tup[-2])

if 4 in tup:
    print("yes")
else:
    print("No")

print(tup[1:3])

#Methods in Tuples
#count

res = tup.count(6)
print(res)

#index
res = tup.index(6, 1, 3)
print(res)