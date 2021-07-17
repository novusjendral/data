# Import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
from playsound import playsound

# Record audio and return it as a string
def recordAudio():
        # Record the audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print('Say Hello!')
                audio = r.listen(source)

        # Speech recognition using Google’s Speech Recognition
        data = ''
        try:
                data = r.recognize_google(audio)
                print('Ucapan Anda: ' + data)
        except sr.UnknownValueError:
                print('Google Speech Recognition could not understand')
        except sr.RequestError as e:
                print('Request error from Google Speech Recognition')
        return str(data)
        

# Function to get the virtual assistant response
def assistantResponse(text):
        print(text)    # Convert the text to speech
        myobj = gTTS(text=text, lang='id', slow=False)

        # Save the converted audio to a file
        myobj.save('assistant_response.mp3')    # Play the converted file
        # os.system(‘start assistant_response.mp3’)
        playsound('assistant_response.mp3')
        os.remove('assistant_response.mp3')

# A function to check for wake word(s)
def wakeWord(text):
        WAKE_WORDS = ['jarvis']
        text = text.lower()  # Convert the text to all lower case words  # Check to see if the users command/text contains a wake word
        for phrase in WAKE_WORDS:
                if phrase in text:
                        return True  # If the wake word was not found return false
        return False

# Function to return a random greeting response
def greeting(text):
        # Greeting Inputs
        GREETING_INPUTS = ['hello', 'halo', 'hello', 'hi','hey','jarvis']     # Greeting Response back to the user
        GREETING_RESPONSES = ['Yes', 'Saya disini MASTER!!']     # If the users input is a greeting, then return random response
        for word in text.split():
                if word.lower() in GREETING_INPUTS:
                        return random.choice(GREETING_RESPONSES) + '.'    # If no greeting was detected then return an empty string
        

# Function to get a person first and last name
def getPerson(text):
        wordList = text.split()# Split the text into a list of words      for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) : 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is'
        return wordList[i + 2]+ ' ' + wordList[i + 3]

while True:
        # Record the audio
        text = recordAudio()
        #print(f'Kata anda adalah {text}')
        response = '' #Empty response string
        # Checking for the wake word/phrase
        if (wakeWord(text) == True):
                # Check for greetings by the user
                print("Loading Response!!")
                response = response + greeting(text)
        else:
                response = "Maaf saya tidak mengerti anda mengatakan " + text       


        # Check to see if the user said tanggal
        # if (‘tanggal’ in text):
        # get_date = getDate()
        # response = response + ‘ ‘ + get_date         # Check to see if the user said waktu
        #         if(‘waktu’ in text):
        # now = datetime.datetime.now()
        # meridiem = ”
        # if now.hour >= 12:
        # meridiem = ‘p.m’ #Post Meridiem (PM)
        # hour = now.hour – 12
        # else:
        # meridiem = ‘a.m’#Ante Meridiem (AM)
        # hour = now.hour           # Convert minute into a proper string
        # if now.minute < 10:
        # minute = ‘0’+str(now.minute)
        # else:
        # minute = str(now.minute)             response = response + ‘ ‘+ ‘It is ‘+ str(hour)+ ‘:’+minute+’ ‘+meridiem+’ .’

        # Check to see if the user said ‘siapa’
        # if (‘siapa’ in text):
        # person = getPerson(text)
        # wiki = wikipedia.summary(person, sentences=2)
        # response = response + ‘ ‘ + wiki

        # Assistant Audio Response
        assistantResponse(response)