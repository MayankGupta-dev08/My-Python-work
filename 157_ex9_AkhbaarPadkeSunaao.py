'''
Using newsapi.org get an api to get daily latest news and use request module and json module and win32com.client module to create a program which reads latest news of that day to you from various internet news sources.

Windoes powershell - pip isntall mywin32
'''

def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":
    speak("Hi, Mayank. Hope you are doing great. You are the best!!")