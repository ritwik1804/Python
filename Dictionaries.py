info = {
    "Name": "Ritwik",
    "Age" : 21,
    "College": "SRM",
    "Profession" : "Student",
    "Country" : "India"
}

print(info)

for keys in info.keys():
    print(info[keys])

print(info.values())

#Dictionary Methods
s1 ={
    1: 100,
    2: 55,
    13: 66,
    57: 90, 
    66: 100
}
s2 = {
    3: 27,
    6: 35,
    10:100
}

#update
s1.update(s2)
print(s1)

#clear
s1.clear()
print(s1)

#empty
s3 = {}
print(type(s3))

#pop
s2.pop(10)
print(s2)

#popitem
s2.popitem()
print(s2)

#del
del s1[13]
print(s1)