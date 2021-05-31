'''Different functions in random module'''

import random
# firstly need to import the module

randNum = random.randint(1,100) 
# Chooses randomly from 1 to 100 including both but only integers.
print(randNum)

rand_natNum = random.random()
# Chooses randomly from 0 to 1 including both but only natural numbers (float).
print(rand_natNum)

rand_natNum = random.random()*100
# Chooses randomly from 0 to 100 including both but only natural numbers (float).
print(rand_natNum)

randChoice = random.choice([1,11,5,9,7])
# Chooses randomly from the list.
print(randChoice)
