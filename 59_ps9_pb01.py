# Reading a text from poem.txt and finding if it contains the word 'twinkle'.

f = open("poem.txt", "r")
data = f.read()
data = data.lower()
c=0
word = input("Enter the word, for search in poem.txt\n")
c = data.count(word)
if word in data:
    print("Yes, it contains your word: "+str(c)+" times.")
else:
    print("No, it doesn't contain: ", word)
f.close()