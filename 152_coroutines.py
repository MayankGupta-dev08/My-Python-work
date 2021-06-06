'''Coroutines in Python
                It's written just like a normal function but it doesn't behave like one.
                It is used when you have to run a function many times but you dont want to start it from the biginning everytime rather it starts from a check point.
                It also uses yield, next() and send() function for its implementation.
        # Suppose the task which is done by the function in biginning is some big task (time taking) and we don't want to do it again and again to increase aour run time.
        # So we will just run this once and it will be stored and used for next execution from the check point.
'''

def searcher():
    import time
    # with open("poem.txt") as f:
    #     content = f.read()
    content = '''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.'''
    time.sleep(5)
    print("Finished reading the poem")
    # We are denoting a time taking task from above line.


    while True:         # This will be the checkpoint.
        text = yield    # we are sending words using send()
        if text in content:
            print("Your text is in the poem.txt\n")
        else:    
            print("Your text isn't in the poem.txt\n")


search = searcher()

print("Starting to read the poem")
next(search) # this line will execute the function for the first time. Initialising it for first time.
print("Search ended at check point.\n")

word = input("Enter your word for next search: ")
print(f"Continuing from check point, Searched - {word}")
search.send(word)
word = input("Enter your word for next search: ")
print(f"Continuing from check point, Searched - {word}")
search.send(word)
word = input("Enter your word for next search: ")
print(f"Continuing from check point, Searched - {word}")
search.send(word)
word = input("Enter your word for next search: ")
print(f"Continuing from check point, Searched - {word}")
search.send(word)
word = input("Enter your word for next search: ")
print(f"Continuing from check point, Searched - {word}")
search.send(word)
search.close()
# NOTE - # After search.close(), our coroutine will not work and all its resources will be relased.
         # If we want to again use it we will agin have to initialize firstly using next(search)