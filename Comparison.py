import speech_recognition as sr

r = sr.Recognizer()  

mysp=__import__("my-voice-analysis")
p="output7_passionate" # Audio File title
c=r"C:\Users\VYBHAV JAIN\Desktop\Tone Analysis" # Path to the Audio_File directory (Python 3.7)
mysp.myspgend(p,c)
#mysp.myspsr(p,c)
mysp.myspatc(p,c)#mysp.myspst(p,c)

r = sr.Recognizer()
with sr.WavFile("output7_passionate.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)   
print("text is: \n" + r.recognize_google(audio))


mysp=__import__("my-voice-analysis")
p="output6_reading" # Audio File title
c=r"C:\Users\VYBHAV JAIN\Desktop\Tone Analysis" # Path to the Audio_File directory (Python 3.7)
mysp.myspgend(p,c)
#mysp.myspsr(p,c)
mysp.myspatc(p,c)#mysp.myspst(p,c)

with sr.WavFile("output6_reading.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)   
print("text is: \n" + r.recognize_google(audio))

