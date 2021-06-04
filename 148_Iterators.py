'''
1. Iterable - Any thing in python which can be loop over. Eg - List, string, Dictionary, tuple, range etc.
              int is not an iterable thing.
              In python an object which implements __iter__() method or __getitem__() method is called an iterable.
              we can check whether an object has {__iter__() or __getitem__()} method or not by using dir() method.

2. Iterators - Iterator in python is an object that can return data one at a time while iterating over an iterable.
               For an object to be an iterator it must implement two methods: __iter__() and __next__()

Why iterators???
    These are powerfull tools when dealing with large set of data so if use regular list to store these values then our computer will run out of memory quickly. So by this we can generate values one by one when we need to and save memory and work with infinite data with limited memory.
    Generally, these are implemented in python with the help of generators which makes then easy to use.
'''

odd1to10 = [1,3,5,7,9]
print(dir(odd1to10), "\n") # This shows that our list has __iter__() method in it.

value = odd1to10.__iter__()
print(value, "\n")
# value = iter(odd1to10) # this could also be written insted of above.
item1 = value.__next__()
# item1 = next(value) # this could also be written insted of above.
print(item1)
item2 = next(value)
print(item2)
item3 = next(value)
print(item3)
item4 = next(value)
print(item4)
item5 = next(value)
print(item5, "\n")
# item6 = next(value)
# print(item6) # here it will throw an error if we will try to print this as their are only 5 elements in list.


'''How for loop actually works --> It actually uses a while loop and breaks on getting false for condition'''

even1to10 = [2,4,6,8,10]
iter_obj = even1to10.__iter__()

while True:
    try:
        element = iter_obj.__next__()
        print(element)
    except StopIteration:
        break



'''Using Class'''
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
print(numbers.__next__())
print(next(numbers))
print(next(numbers))
print(next(numbers))