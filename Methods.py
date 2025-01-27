#Class Methods
class Employee:
    company = "Apple"
    def show(self):
        
        print(f"name is {self.name} and works for the company {self.company}")

    @classmethod  
    def changeCompany(cls, newCompany):
            cls.company = newCompany

e1 = Employee()
e1.name = "Ritwik"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)

#Class Methods as Alternative Constructor
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
     return cls(string.split("-")[0], string.split("-")[1])

e1 = Employee("Hari", 1400000)
print(e1.name)
print(e1.salary)

string = "RM-100000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)

#dir() method
x= [1,2,3]
print(dir(x))
print(x.__add__)

#__dict__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("rm", 21)
print(p.__dict__)

#help
#print(help(Person))

#super keyword
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
a= Employee("ab","400")
b = Programmer("a", "2345", "Python")
print(b.name)
print(b.id)
print(b.lang)


#Dunder Methods/ Magic Methods
class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i=0
        for c in self.name:
            i = i+1
        return i

#e = Employee("Ritwik")
#print(e.name)
#print(len(e))

    def __str__(self):
        return f"The name of the employee is {self.name} str"
    def __repr__(self):
        return f"The name of the employee is {self.name} repr"
    def __call__(self, *args, **kwds):
        print("Hey all good")

#Method overriding
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self. y