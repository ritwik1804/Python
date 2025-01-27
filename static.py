class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n
    
    @staticmethod
    def add(a,b):
        return a + b
    
a= Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(Math.add(7, 2))
#print(add(7,2))


#Instance variable vs class Variable
#Instance Variable
class Employee:
    def __init__(self, name):
        self.name = name
        self. raise_amount = 0.02
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and raise amount is {self.raise_amount}")

emp1 = Employee("Ritwik")
emp1.raise_amount = 0.3
emp1.showDetails()
emp2 = Employee("Hari")
emp2.showDetails()

#Class Variable
class Employee:
    company_name = "Apple"
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and raise amount is {self.raise_amount} works in {self.company_name}")

emp1 = Employee("RM")
emp1.raise_amount = 0.3
emp1.company_name = "Apple India"
emp1.showDetails()
Employee.company_name = "Google"
print(Employee.company_name)

emp2 = Employee("Hari")
emp2.raise_amount = 0.5
emp2.showDetails()