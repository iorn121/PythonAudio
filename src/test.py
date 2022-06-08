from calendar import c
import wave as wave
from utils import save_sound_wave,save_sound_info,record_sound
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

name='test'
record_sound(5,16000,name)
data=wave.open("./WAV/test.wav","rb")
buff=data.readframes(-1)
convert=np.frombuffer(buff,dtype=np.int16)
fig=plt.figure(figsize=(10,4))
spectrum,freqs,t,im=plt.specgram(convert,NFFT=512,noverlap=512/16*15,Fs=data.getframerate(),cmap="gray")
fig.colorbar(im).set_label('Intensity [dB]')
plt.xlabel('Time [sec]')
plt.ylabel('Frequency [Hz]')
plt.savefig('./jihou_tadaima_spectrum.png')
plt.show()