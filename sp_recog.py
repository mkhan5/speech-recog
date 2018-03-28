
# Requires PyAudio and PySpeech.

import speech_recognition as sr

#Sample rate is how often values are recorded
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) here.
#it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048

r = sr.Recognizer()
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Micro name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
#exit()
with sr.Microphone(device_index = 0, sample_rate = sample_rate,
                        chunk_size = chunk_size) as source:
    #wait for a second to let the recognizer adjust the
    #energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
print("Done Listening")

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


exit()

# Read recorded audio
#from os import path
#AUDIO_FILE = path.join(path.dirname(path.realpath("input/")), "rec1.wav")
#with sr.AudioFile("input/rec1.wav") as source:
#    audio = r.record(source) # read the entire audio file
#print("Done Listening")

#Record audio usind sounddevice module (for laptop mic)
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

fs=44100
duration = 5  # seconds
myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
print "Recording Audio"
sd.wait()
print "Audio recording complete , Play Audio"
sd.play(myrecording, fs)
sd.wait()
print "Play Audio Complete"
#IMP
#The recorded audio can be saved as wav file
#exit()
