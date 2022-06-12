import numpy as np
import matplotlib.pyplot as plt
import wave as wave
import sounddevice as sd
# import soundfile as sf
import logging
import os


def play_sound(data_np, frame_rate):
    sd.play(data_np, frame_rate)
    print("Play sound...")
    status = sd.wait()


def record_sound(second_length, frame_rate, name):
    print("Record...")
    data = sd.rec(int(second_length*frame_rate), frame_rate, channels=1)
    sd.wait()
    print("Complete")
    # ノーマライズ。量子化ビット16bitで録音するので int16 の範囲で最大化する
    data = data / data.max() * np.iinfo(np.int16).max

    # float -> int
    data = data.astype(np.int16)
    # Macではsoundfileがエラー起こして動かせないっぽい
    # sf.write('./WAV/'+name+'.wav', data, frame_rate)
    save_wave_file(data, frame_rate, name)


def save_wave_file(data_np, frame_rate, name):
    with wave.open('./WAV/'+name+'.wav', mode='wb') as wb:
        wb.setnchannels(1)  # モノラル
        wb.setsampwidth(2)  # 16bit=2byte
        wb.setframerate(frame_rate)
        wb.writeframes(data_np.tobytes())  # バイト列に変換


def save_sound_info(data_wav, name):
    info = data_wav.getparams()
    f = open(name+"_info.txt", 'w')
    params = ['nchannels', 'sampwidth', 'framerate',
              'nframes', 'comptype', 'compname']
    for p, i in zip(params, info):
        print(p, i)
        f.write(p+': '+str(i)+'\n')
    f.close()


def convert_wave_to_np(data_wav):
    buff = data_wav.readframes(-1)
    convert = np.frombuffer(buff, dtype=np.int16)
    return convert


def save_sound_wave(data_np, channel_n, name):
    if channel_n == 2:
        data_np_l = data_np[::2]
        data_np_r = data_np[1::2]
        plt.subplot(211)
        plt.plot(data_np_l)
        plt.subplot(212)
        plt.plot(data_np_r)
    else:
        plt.plot(data_np)
    plt.savefig(name+"_wave.png")


def save_sound_frequency(data_np, frame_rate, name):
    fig = plt.figure(figsize=(10, 4))
    spectrum, freqs, t, im = plt.specgram(
        data_np, NFFT=512, noverlap=512/16*15, Fs=frame_rate, cmap="gray")
    fig.colorbar(im).set_label('Intensity [dB]')
    plt.xlabel('Time [sec]')
    plt.ylabel('Frequency [Hz]')
    plt.savefig('./'+name+'_spectrum.png')
    plt.show()
