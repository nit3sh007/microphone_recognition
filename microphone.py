import speech_recognition as sr

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    # adjust_for_ambient_noise use to ambient noise
    #r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:

    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))