'''PICKLE MODULE

Python pickle module is used for serializing and de-serializing python object structures. The process to converts any kind of python objects (list, dict, str, int etc.) into byte streams (0s and 1s) is called pickling or serialization or flattening or marshalling. We can converts the byte stream (generated through pickling) back into python objects by a process called as unpickling.

Why Pickle?: 
        In real world sceanario, the use pickling and unpickling are widespread as they allow us to easily transfer data from one server/system to another and then store it in a file or database.

Precaution: 
        It is advisable not to unpickle data received from an untrusted source as they may pose security threat. However, the pickle module has no way of knowing or raise alarm while pickling malicious data.

Below are some of the common exceptions raised while dealing with pickle module −
    Pickle.PicklingError: If the pickle object doesn’t support pickling, this exception is raised.
    Pickle.UnpicklingError: In case the file contains bad or corrupted data.
    EOFError: In case the end of file is detected, this exception is raised.

Prons:
    Comes handy to save complicated data.
    Easy to use, lighter and doesn’t require several lines of code.
    The pickled file generated is not easily readable and thus provide some security.

Cons:
    Languages other than python may not able to reconstruct pickled python objects.
    Risk of unpickling data from malicious sources.
'''

import pickle #built-in module

cars = ["Toyota Motors", "Volkswagen", "Daimler", "Ford Motor", "Audi", "BMW", "Tata Motors", "Kia", "Suzuki", "Volvo", "Renailt", "Honda Motor", "General Motors", "Hyundai", "Nissan", "Fiat Chrysler"]

# use of pickel.dump() to pickle data in binary format
file = "myCars.txt"
fobj = open(file, "wb")
pickle.dump(cars, fobj)
fobj.close()

# use of pickel.load() to get that pickled data in its original form. 
import pickle

fobj = open(file, "rb")
mycars = pickle.load(fobj)
# print(mycars)
for i, j in enumerate(mycars):
    print(f"{i+1}.  {j}")
print(type(mycars))
fobj.close()
# pickle.load is used to load pickled data from a file-like object. This is any object that acts like a file - in this case, meaning it has a read() method that returns bytes

# pickle.loads is used to load pickled data from a bytes string. The "s" in loads refers to the fact that in Python 2, the data was loaded from a string

import pickle

with open("myCars.txt", "rb") as f:
    rawdata = f.read()

myobj = pickle.loads(rawdata)
print(rawdata)