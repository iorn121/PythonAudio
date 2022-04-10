import wave as wave
import numpy as np


sample_wave_file = './WAV/file_example_WAV_1MG.wav'

wav = wave.open(sample_wave_file)

print('サンプリング周波数[Hz]', wav.getframerate())
print('サンプルサイズ[Byte]', wav.getsampwidth())
print('サンプル数', wav.getnframes())
print('チャンネル数', wav.getnchannels())

data = wav.readframes(wav.getnframes())

data = np.frombuffer(data, dtype=np.int16)

wav.close()
