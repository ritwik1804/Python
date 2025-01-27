#Set is a unordered collection of data items. it does not take repeated values
s= {2,4,2,7,5,4}
print(s)
print(type(s))

ritwik = set()
print(type(ritwik))

#set Methods
s1={2,3,4,2,5,6}
s2= {1,2,5,3,4,7}

#union
#print(s2.union(s1))

#update
#s1.update(s2)
#print(s1, s2)

#intersection
s3= s1.intersection(s2)
print(s3)

#intersection_update
#s1.intersection_update(s2)
#print(s1, s2)

#symmetric_difference
#s4 = s2.symmetric_difference(s1)
#print(s4)

#difference
#s5= s1.difference(s2)
#print(s5)

#isdisjoint()
print(s1.isdisjoint(s2))

#issuperset
print(s2.issuperset(s1))

#issubset()
print(s3.issubset(s2))

#add()
s1.add(9)
print(s1)

#update
s1.update(s2)
print(s1)

#remove()/discard()
s1.discard(8)
#s1.remove(8)
print(s1)

#pop()
item = s1.pop()
print(item)

#del
s2.clear()
print(s2)
