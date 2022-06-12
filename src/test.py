import wave as wave
from utils import save_sound_wave, save_sound_info, record_sound, save_sound_frequency, play_sound, convert_wave_to_np, save_wave_file
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

name = 'test'
frame_rate = 16000
# record_sound(5, frame_rate, name)
data_wav = wave.open('./WAV/test.wav')
data_np = convert_wave_to_np(data_wav)
f, t, stft_data = sp.stft(data_np, fs=frame_rate, window='hann',
                          nperseg=512, noverlap=256)
stft_data[:50, :] = 0
t, data_post = sp.istft(stft_data, fs=frame_rate,
                        window='hann', nperseg=512, noverlap=256)
play_sound(data_np, frame_rate)
