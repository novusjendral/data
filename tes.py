from gtts import gTTS
import os
from playsound import playsound
while True:
    text = input("masukan text: ")
    tts = gTTS(text, lang='jw',slow=False)
    tts.save('hello.mp3')
    playsound('hello.mp3')
    os.remove('hello.mp3')