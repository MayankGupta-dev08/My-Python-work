'''
Acess Modifiers for attributes in Python
Example for Public, Protected and Private attributes
Public - Normally as you do.
Protected - Can be access from your class, derived classes and their objects. Syntax: _nameOfAttribute
Private - Can only be access within your class from their methods aka member functions. Syntax: __nameOfAttribute
            If we want to acess it from the object of that class then we have to use classtName and it is known as Name Handling.  Syntax: _FunctionName__nameOfAttribute
'''

class Company:
    company_name = "TATA & SONS"
    location = "India"
    _Owner = "Mr. Ratan Tata" # protected variable
    __revenue = "USD 5000 Bn" # private variable

    def showDetails(self):
        print(f"This is {self.company_name} Company and its owner is {self._Owner}.")
        print(f"The company's revenue is {self.__revenue}.")

class Subsidiary(Company):
    company_name = "TCS"
    work = "Consultancy"
    def showDetails(self):
        print(f"This is {self.company_name} Subsidiary Company and its work is {self.work}.")

class Programmer(Subsidiary):
    name  = "Mannu"
    language = "Python"
    def showDetails(self):
        print(f"Hi, I am {self.name} and I am a Programmer, having proficiency in {self.language}.")

p = Programmer()
p.showDetails()
print(p.company_name)
print(p.location)
print(p.work)
s=Subsidiary()
s.showDetails() # Subsidiary.showDetails(p) #--> works same.
print(s._Owner) # We can acess protected variable from derived class object or member fuction.
c=Company()
c.showDetails() # Company.showDetails(p) #--> works same.
# print(s.__revenue) # We can't acess private variable from derived class object or member fuction.
# print(c.__revenue) 
# We can't normally acess private variable from derived class object, but if we ant to do that than we have to use Name Handling.
print(c._Company__revenue)


'''program to illustrate protected data members in a class'''

# super class
class Shape:
	
	def __init__(self, length, breadth):
		self._length = length
		self._breadth = breadth
		
	def displaySides(self):

		print("Length: ", self._length)
		print("Breadth: ", self._breadth)


class Rectangle(Shape):

	def __init__(self, length, breadth):

		# Calling the constructor of Super class
		Shape.__init__(self, length, breadth)
		
	def calculateArea(self):
					
		# accessing protected data members of super class
		print("Area: ", self._length * self._breadth)
					

obj = Rectangle(80, 50)
print("\n")
obj.displaySides()
obj.calculateArea()
