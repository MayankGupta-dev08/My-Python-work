import random
def game():
    """This is a doc string which is used to explain what does this function does or what it is meant for doing and it is always the first line in the function if used."""
    a = random.randint(1,1000)
    print("Randomly generated number: ", a)

print(game.__doc__) # Prints line3
game()