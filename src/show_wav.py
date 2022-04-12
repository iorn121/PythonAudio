import wave as wave
import numpy as np
import matplotlib.pyplot as plt


sample_wave_file = './WAV/file_example_WAV_1MG.wav'

wav = wave.open(sample_wave_file)

print('サンプリング周波数[Hz]', wav.getframerate())
print('サンプルサイズ[Byte]', wav.getsampwidth())
print('サンプル数', wav.getnframes())
print('チャンネル数', wav.getnchannels())

data = wav.readframes(wav.getnframes())

data = np.frombuffer(data, dtype=np.int16)


data = data/np.iinfo(np.int16).max
x = np.array(range(2*wav.getnframes()))/wav.getframerate()
plt.figure(figsize=(10, 4))
plt.xlabel('Time[sec]')
plt.ylabel('Value[-1,1]')
plt.plot(x, data)
plt.savefig('./IMG/wave_form.png')
plt.show()

wav.close()
