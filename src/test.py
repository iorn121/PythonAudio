import wave as wave
from utils import save_sound_wave,save_sound_info
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

data=wave.open("./WAV/jihou_tadaima.wav","rb")
buff=data.readframes(-1)
convert=np.frombuffer(buff,dtype=np.int16)
f,t,stft_data=sp.stft(x=convert,fs=data.getframerate(),window='hann',nperseg=512,noverlap=256)

print(f,t,stft_data)