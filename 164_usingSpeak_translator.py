'''Not working try to find the solution'''

# from googletrans import Translator
# import win32com.client as wincl
# translator = Translator()

# a=translator.translate('Harry Brother is very brilliant really',src='en',dest='hi')
# print (a.text)
# speak = wincl.Dispatch("SAPI.SpVoice")
# speak.Speak(a.text)


'''Another thing, Way to change the voice of speaker'''
import win32com.client as wincl

speaker_number = 0
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
# SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
spk.Speak("Hello, it works!")

speaker_number = 1
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
spk.Speak("Hello, it works!")