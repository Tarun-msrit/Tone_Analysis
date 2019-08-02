from watson_developer_cloud import ToneAnalyzerV3

#from ibm_watson import ToneAnalyzerV3

import speech_recognition as sr

r = sr.Recognizer()  
with sr.Microphone() as source:
    print('Say Something')
    #r.adjust_for_ambient_noise(source)
    #print("Set minimum energy threshold to {}".format(r.energy_threshold))
    audio=r.listen(source)
    
n=r.recognize_google(audio)
print(n)

tone_analyzer = ToneAnalyzerV3(
    version='2019-07-24',
    iam_apikey='wmqMO8skAUwE37yE7vT2DuvfRp4qj4vWmyg4l8f-mePC',
    url='https://gateway-lon.watsonplatform.net/tone-analyzer/api')

#msg = 'happy to inform you that you failed the job!!'
#msg = 'I am so happy'
json_output = tone_analyzer.tone(n, content_type='text/plain')
print(json_output.result) #