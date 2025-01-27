#Single Inheritance
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Sound made by animal")
    
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("bark")
        

d= Dog("Dog", "Cat")
d.make_sound()

a = Animal("Tiger", "Lion")
a.make_sound()

#Multiple Inheritance
class Employee:
    def __init__(self, name):
        self.name = name

class Dance:
    def __init__(self, dance):
        self.dance = dance

class DancerEmployee(Employee, Dance):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

o = DancerEmployee("Ritwik", "RM")
print(o.name)
print(o.dance)
print(DancerEmployee.mro)

#Multilevel Inheritance

class Animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def show_details(self):
        print(f"name {self.name}")
        print(f"species {self.species}")

class Dogs(Animals):
    def __init__(self, name, breed):
        Animals.__init__(self, name, species = "Dogs")
        self.breed = breed
        

    def show_details(self):
        Animals.show_details(self)
        print(f"breed {self.breed}")

class GoldenRetrival(Dogs):
    def __init__(self, name, color):
        Dogs.__init__(self, name, breed = "GoldenRetrival")
        
        self.color = color

    def show_details(self):
        Dogs.show_details(self)
        print(f"color: {self.color}")

o = GoldenRetrival("toomy", "black")
o.show_details()

#mro is method resolution order

#Hybrid Inheritance
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1, Derived2):
    pass

#Hierarchial Inheritance
class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass

class D3(D1):
    pass


        



        

