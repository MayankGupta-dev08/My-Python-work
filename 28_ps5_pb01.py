# Write a program to create a Dict containing Hindi Words as Key and their English Translations as Values, allowing the user to provide the word and you print the associated Value of that key.

Dict1 = {
    "Bhai":"Brother",
    "Behn":"Sister",
    "Pankhha":"Fan",
    "Namaste":"Hello",
    "Mummy":"Mom",
    "Papa":"Dad",
    "Paani":"Water",
}

print("Your options for words are: ", Dict1.keys())
a = input("Enter your Hindin word from the options: \n")
print("WARNING: If you will enter any word other than options than it will show None as the Answer.\n")
print("English translations for your Hindi word is: ", Dict1.get(a))