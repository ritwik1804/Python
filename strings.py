#f-strings this is used to solve string formatting
country = "India"
name = "Ritwik"

print(f"Hey, My name is {name} and I an from {country}")

Price = 5000000
years = 25

print(f"Hey , Whats the price of this house. It costs {Price} and it will take {years} years to be ready ")

#DocStrings and pep- 8
def square(n):

    print(n**2)
square(5)
print(square.__doc__)


