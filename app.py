from GoogleNews import GoogleNews as gn
import pyttsx3
from PyDictionary import PyDictionary

class Speaking:
    def speak(self, audio):
        engine = pyttsx3.init('sapi5')     
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()
speak = Speaking()
News = gn()
News = gn(period='7d')
News.search(input('Search Anything:'))
result = News.result(sort=True)
print("Welcome to Artificial News Anchor Using Python by Vinayak  Sir")
speak.speak("Welcome to Artificial News Anchor Using Python by Vinayak Sir")
for x in result:
    print("--"*100)
    print("Headline: ",x['title'])
    speak.speak("Headline" + str(x['title']))
    print("Time:",x['date'])
    speak.speak("Time: "+str(x['date']))
    print("Description: ",x['desc'])
    speak.speak("Description:"+str(x['desc']))
    print("Media Source: ",x['media'])
    speak.speak("Source "+str(x['media']))
    print("Full Article: ",x['link'])
    speak.speak("For more details click on this link")

