from calendar import c
import wave as wave
from utils import save_sound_wave, save_sound_info, record_sound, save_sound_frequency, play_sound
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

name = 'test'
frame_rate = 16000
data = record_sound(5, frame_rate, name)

f, t, stft_data = sp.stft(
    data, fs=frame_rate, window='hann', nperseg=512, noverlap=256)
stft_data[100:, :] = 0
t, data_post = sp.istft(stft_data, fs=frame_rate,
                        window='hann', nperseg=512, noverlap=256)
save_sound_wave(data_post, name)
play_sound(data_post, frame_rate)
