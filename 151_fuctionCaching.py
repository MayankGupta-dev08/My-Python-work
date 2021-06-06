'''Function Caching  - It is the way we try to store cache/results of the previous runs and use them later if same arguments were passed again.
                       It saves time.
Syntax or things used:
                    from functools import lru_cache
                    @lru_cache(maxsize=)
'''

import time
from functools import lru_cache

c = int(input("How many differnet values do u want to be cached: "))    
# last c different results will be cached as maxsize = c, and can be used again without executing function again.
@lru_cache(maxsize=c)
def someWork(n):
    # Just for example some work in this function will take n seconds
    time.sleep(n)
    # print(n)
    return n

if __name__ == "__main__":
    print("Now running someWork() function which is being cached")
    print(someWork(2))
    print(someWork(3))
    print(someWork(4)) # These values will be cached as it is one of the last two different ones.  
    print(someWork(5)) # These values will be cached as it is one of the last two different ones.
    print("Done! Calling it again........")
    print(someWork(5)) # This value will be given using cached data and not by executing function.
    print(someWork(4)) # This value will be given using cached data and not by executing function.
    print(someWork(3))
    print("Called it again..")