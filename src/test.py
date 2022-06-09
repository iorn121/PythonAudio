import wave as wave
from utils import save_sound_wave, save_sound_info, record_sound, save_sound_frequency, play_sound
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

name = 'test'
frame_rate = 16000
# record_sound(5, frame_rate, name)
data=wave.open('./WAV/test.wav')
print(type(data))
buff = data.readframes(-1)
convert = np.frombuffer(buff, dtype=np.int16)
f, t, stft_data = sp.stft(
    x=convert,fs=frame_rate, window='hann', nperseg=512, noverlap=256)
stft_data[100:, :] = 0
t, data_post = sp.istft(stft_data, fs=frame_rate, window='hann', nperseg=512, noverlap=256)

fig = plt.figure(figsize=(10, 4))
spectrum, freqs, t, im = plt.specgram(
    data_post, NFFT=512, noverlap=512/16*15, Fs=data.getframerate(), cmap="gray")
fig.colorbar(im).set_label('Intensity [dB]')
plt.xlabel('Time [sec]')
plt.ylabel('Frequency [Hz]')
plt.savefig('./'+name+'_post_spectrum.png')
plt.show()
with wave.open('./WAV/'+name+'_post.wav', mode='wb') as wb:
    wb.setnchannels(1)  # モノラル
    wb.setsampwidth(2)  # 16bit=2byte
    wb.setframerate(frame_rate)
    wb.writeframes(data_post.tobytes())  # バイト列に変換
