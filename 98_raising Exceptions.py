def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not good :(")

print(increment(5))
print(increment("bnj5"))