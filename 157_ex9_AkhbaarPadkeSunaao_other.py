import requests
import json
from win32com.client import Dispatch

def speak(string):
    speak=Dispatch('SAPI.spVoice')
    speak.speak(string)

url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=ba4edb5b19e04598b7f4740a0ea716f7')
data=requests.get(url=url)
india=data.json() # Here we are directly using json object

print("Welcome to the Mayank's News Channel")
speak("Welcome to the Mayank's News Channel")
print("Here are the top news of our awesome country India\n")
speak("Here are the top news of our awesome country India")

for i in range(20):
    print(i,india['articles'][i]['source']['name'])
print("")

try:
    while True:
        speak("choose newspaper by entering its number. For exiting enter any word")
        num=int(input("choose newspaper by entering its number. For exiting enter any word\n"))
        if num>=0 and num<=20:
            speak("So the news is")
            print(india['articles'][num]['title'])
            speak(india['articles'][num]['title'])
            speak(india['articles'][num]['description'])
            print(india['articles'][num]['content'])
            print("For more info:\n",india['articles'][num]['url'], "\n")
        else:
            print("Please enter a valid input")
except Exception as e:            
    print("Exiting the news channel.....")
finally:
    print("Thanks for listening ! Have a nice day")
    speak("Thanks for listening ! Have a nice day")