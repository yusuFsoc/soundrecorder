import sounddevice as sd
from scipy.io.wavfile import write

file_name = input("kaydedilecek dosya ismi veriniz: ")
duration = int(input("kaydedilecek süreyi veriniz: "))

def recorder(freq):
    recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
    sd.wait()
    write(file_name + ".wav", freq, recording)

recorder(44100)

