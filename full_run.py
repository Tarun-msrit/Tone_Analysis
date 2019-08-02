import sounddevice as sd
import wavio
import speech_recognition as sr
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2019-07-24',
    iam_apikey='wmqMO8skAUwE37yE7vT2DuvfRp4qj4vWmyg4l8f-mePC',
    url='https://gateway-lon.watsonplatform.net/tone-analyzer/api')

fs = 44100  # Sample rate
seconds = 8  # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished

wavio.write('output5.wav', myrecording, fs ,sampwidth=2)

r = sr.Recognizer()
with sr.WavFile("output5.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file
 
print("text is: \n" + r.recognize_google(audio))

json_output = tone_analyzer.tone(r.recognize_google(audio), content_type='text/plain')
print(json_output.result) 