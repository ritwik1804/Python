#Classes and Objects
#class Person:
 #   name = "Ritwik"
  #  age = 21
  #  occupation = "Software eng"

  #  def info(self):
  #      print(f"{self.name} is a {self.occupation}")

#a= Person()
#print(a.name, a.occupation)
#a.info()

#self is reference to the parameter of the class and used across the variables that belong to clas


#Constructors
class Person:

    def __init__(self, n, o):
        print("Hey i am a person")
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Ritwik", "Developer")
b = Person("Div", "HR")
a.info()
b.info()


#Decorators

def greet(fx):
    def mfx(*args, **kwargs):
        print("Hii")
        fx(*args, **kwargs)
        print("Thanks for using function")
    return mfx

@greet  
def Hello():
    print("Hello World")      

Hello()
#greet(Hello)()


#Getters and Setters
class Myclass:
    def __init__(self, value):
        self.value = value
        
    def show(self):
        print(f"Value is {self.value}")
    
    @property
    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10

obj = Myclass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()


#Inheritance in Python
#class Employee:
 #   def __init__(self,name, id):
 #       self.name = name
 #    def showDetails(self):
  #      print(f"The name of Employee {self.id} is {self.name}")

#class Programmer(Employee):
#    def showlang(self):
 #       print("The default language is python")

#e1 = Employee("Ritwik", 400)
#e1.showDetails()
#e2 = Programmer("Hari", 18)
#e2.showDetails()

#access specifier
class Employee:
    def __init__(self):
        self.__name = "Ritwik"

a = Employee() # cannot be accessed directly
print(a._Employee__name)# can be access indirectly
print(a.__dir__())

