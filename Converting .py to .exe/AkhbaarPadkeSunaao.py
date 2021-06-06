'''
Using newsapi.org get an api to get daily latest news and use request module and json module and win32com.client module to create a program which reads latest news of that day to you from various internet news sources.

Windoes powershell - pip isntall mywin32
'''
from win32com.client import Dispatch
import requests
import json
from datetime import date

def speak(str):
    spk = Dispatch("SAPI.SpVoice")
    spk.Speak(str)

if __name__ == "__main__":
    td = date.today()
    print(f"Hi, Today is {td} and Lets begin today's news")
    speak(f"Hi, Today is {td} and Lets begin today's news")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=ba4edb5b19e04598b7f4740a0ea716f7"
    news = requests.get(url).text
    # print(news) # json object
    news_dict = json.loads(news) # Converting json to python, here json obj to dictionary
    atc_list = news_dict["articles"]
    # in news_dict, with articles as a key we have a list which we have stored in atc, in this list we have many dicts which are having differeent news.
    # print(atc_list)
    for i, artc_d in enumerate(atc_list):
        if i < len(atc_list)-1:
            speak(f"News {i+1} is")
            print(f"News{i+1}:  ", artc_d["title"])
            speak(artc_d["title"])
            # speak(artc_d["content"])
            print(artc_d["content"],"\nFor More Info: ")
            print(artc_d["url"],"\n")
            speak("So now, moving on to the next news of today")
        else:
            speak(f"Today's final news from us!")
            print(f"News{i+1}:  ", artc_d["title"])
            speak(artc_d["title"])
            # speak(artc_d["content"])
            print(artc_d["content"],"\nFor More Info: ")
            print(artc_d["url"],"\n")
            speak("Thanks for listening patiently, hope to see you tomorrow again!")