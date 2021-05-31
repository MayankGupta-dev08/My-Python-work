# Write a class Calculator to do some basic operations apart from cube, square and squareroot of a number.

import math
class Calculator:
    def __init__(self):
        print("\n\t<No. of Options in Calculator>")
        print("\t\t1. Addition")
        print("\t\t2. Subtraction")
        print("\t\t3. Multiplication")
        print("\t\t4. Division")
        print("\t\t5. Square")
        print("\t\t6. Square root")
        print("\t\t7. Cube")
        print("\t\t8. Cube root")
        print("\t\t9. Exit")
        
    def getinfo(self):
        self.o = int(input("Enter the option number: "))
        if self.o not in range(1,10):
            print("Invalid option number entered!\n")
            self.getinfo()
        elif self.o == 9:
            exit()
        else:
            self.operation()
    
    def operation(self):
        if self.o in range(1,5):
            self.a = float(input("\nEnter the 1st number: "))
            self.b = float(input("Enter the 2nd number: "))
            if self.o == 1:
                print(f"Sum is: {self.a+self.b}\n")
            elif self.o == 2:
                print(f"Difference is: {self.a-self.b}\n")
            elif self.o == 3:
                print(f"Multiplication is: {self.a*self.b}\n")
            else:
                print(f"Division is: {self.a/self.b}\n")

            self.getinfo()
            
        elif self.o in range(5,9):
            self.a = float(input("\nEnter the your number: "))
            if self.o == 5:
                print(f"Sqaure of {self.a} is: {self.a**2}\n")
                # print(f"Sqaure of {self.b} is: {self.a*self.a}\n")
            elif self.o == 6:
                print(f"Sqaureroot of {self.a} is: {math.sqrt(self.a)}\n")
                # print(f"Sqaureroot of {self.a} is: {self.b**0.5}\n")
            elif self.o == 7:
                print(f"Cube of {self.a} is: {self.a**3}\n")
            elif self.o == 8:
                print(f"Cube of {self.a} is: {self.a**(1./3)}\n")
            
            self.getinfo()

calc = Calculator()
calc.getinfo()