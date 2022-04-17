import wave as wave
from matplotlib import scale
import numpy as np
import matplotlib.pyplot as plt


def show_and_save_wave(wav_file):

    print('サンプリング周波数[Hz]', wav_file.getframerate())
    print('サンプルサイズ[Byte]', wav_file.getsampwidth())
    print('サンプル数', wav_file.getnframes())
    print('チャンネル数', wav_file.getnchannels())

    data = wav_file.readframes(wav_file.getnframes())

    data = np.frombuffer(data, dtype=np.int16)

    data = data/np.iinfo(np.int16).max
    x = np.array(range(wav_file.getnchannels()*wav_file.getnframes())) / \
        wav_file.getframerate()
    plt.figure(figsize=(10, 4))
    plt.xlabel('Time[sec]')
    plt.ylabel('Value[-1,1]')
    plt.plot(x, data)
    plt.savefig('./IMG/wave_form.png')
    plt.show()

    wav_file.close()


# ファイルを読み込んで図示
# sample_wave_file = './WAV/file_example_WAV_1MG.wav'
# wav = wave.open(sample_wave_file)
# show_and_save_wave(wav)

# 音声データを書き込む
np.random.seed(0)
n_sample = 40000
sample_rate = 16000
data_write = np.random.normal(scale=0.1, size=n_sample)
data_scale_adjust = data_write*np.iinfo(np.int16).max
data_scale_adjust = data_scale_adjust.astype(np.int16)
wave_out = wave.open('./WAV/file_example_WAV_1MG_write.wav', 'wb')
wave_out.setnchannels(1)
wave_out.setsampwidth(2)
wave_out.setframerate(sample_rate)
wave_out.writeframes(data_scale_adjust)
wave_out.close()
