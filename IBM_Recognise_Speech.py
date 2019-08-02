from watson_developer_cloud import ToneAnalyzerV3
import json
from ibm_watson import SpeechToTextV1

service = SpeechToTextV1(
    url='https://gateway-lon.watsonplatform.net/speech-to-text/api',
    iam_apikey='tSgu5o_HfJTxbR3dKILSPq5200mXZSl8d3nkzAesuD3l')

with open('output4.wav','rb') as audio_file:
    t= json.dumps(service.recognize(audio=audio_file,content_type='audio/wav').get_result(),indent=2)
    y = json.loads(t)
    n = y["results"][0]["alternatives"][0]["transcript"]
    print(n)
    
tone_analyzer = ToneAnalyzerV3(
    version='2019-07-24',
    iam_apikey='wmqMO8skAUwE37yE7vT2DuvfRp4qj4vWmyg4l8f-mePC',
    url='https://gateway-lon.watsonplatform.net/tone-analyzer/api')

json_output = tone_analyzer.tone(n, content_type='text/plain')
print(json_output.result) #