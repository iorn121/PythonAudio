import wave as wave
from utils import save_sound_wave,save_sound_info
import numpy as np
import matplotlib.pyplot as plt

data=np.random.normal(scale=0.1,size=5000)
data_scale_adjust=data*np.iinfo(np.int16).max
print(np.iinfo(np.int16))
plt.hist(data_scale_adjust, bins=100)
plt.show()