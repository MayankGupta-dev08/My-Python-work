'''Creating a generator function for fibonacci series using yield and next()'''
# NOTE - yield and next()

def fibonacci_genr():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n1, n2 = n2, n1+n2

num = int(input("Enter the number of digits you want in your fibnoacci series: "))
seq = fibonacci_genr()
for i in range(0,num):
    print(next(seq), end=" ")
print("\n\n")


'''Creating a generator function for generating an infinite stream of odd numbers and then printing first 10.'''
# NOTE - Use yield and next()

def oddNum_genr():
    n1 = 1
    while True:
        yield n1
        n1 += 2

series = oddNum_genr()
for i in range(0,10):
    print(next(series), end=" ")
print("\n\n")


'''Creating a generator function for generating an infinite stream of even numbers and then printing first 10.'''
# NOTE - Use yield and next()

def evenNum_genr():
    n1 = 0
    while True:
        yield n1
        n1 += 2

series = evenNum_genr()
for i in range(0,10):
    print(next(series), end=" ")
print("\n\n")


'''Creating a generator function for factorial using yield and next()'''
# NOTE - yield and next()

def fact_genr():
    n1 = 1
    while True:
        yield n1
        n1 +=1

if __name__ == "__main__":    
    num = int(input("Enter the number for which you want factorial: "))
    if num>=0:
        fact =1    
        f = fact_genr()
        for i in range(0,num):
            fact = fact*next(f)
        print(fact)
    elif num==0:
        print(1)
    else:
        print("Enter a positive integer")