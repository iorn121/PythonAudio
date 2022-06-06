import wave as wave
from utils import save_sound_wave,save_sound_info
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

data=wave.open("./WAV/jihou_tadaima.wav","rb")
