'''
PYTHON GENERATORS
    As we already know that why we need iterators and we have seen how they can be implemented in our last example. So we know it can be quite lengthy to work with in case of large stream of data.
    So with python generators we can do this work quite easily and automatically.

How to make a function iterator??
    If we will use 'yield' keyword inside the function with correct logic than function will work like an iterator.


Difference between yield and return statement??
    return statement terminates the function completely whereas yield statement pauses the function saving all its states for the next successive calls, so when we call the fuction for the next time it will give us the next possibe value. 

Why??
    These are used to create our custom iterator functions.
    With the use of generators we don't have to explicitly define __iter__() or __next__() or even a StopIteration Exception, and our work becomes easier.
'''
class Even:
    def __init__(self, num):
        self.n = 2
        self.max = num
        print("")

    def __iter__(self):
        return self

    def __next__(self):
        if self.n<= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration("Nothing more to loop over!!")

numbers = Even (10)
print(next(numbers))
print(next(numbers))
print(next(numbers), "\n\n")


# The below code works same as above one but its comparitively very small with the use of yield.
def even_Generators(max):
    n=2
    while n<=max:
        yield n
        n+=2

numbers = even_Generators(10) 
print(next(numbers))
print(next(numbers))
print(next(numbers))
