import sounddevice as sd
import wavio

fs = 44100  # Sample rate
seconds = 10  # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished

wavio.write('output7.wav', myrecording, fs ,sampwidth=2)
