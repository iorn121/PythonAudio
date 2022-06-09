import numpy as np
import matplotlib.pyplot as plt
import wave as wave
import sounddevice as sd
# import soundfile as sf
import logging
import os


def play_sound(data, frame_rate):
    sd.play(data, frame_rate)
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

    with wave.open('./WAV/'+name+'.wav', mode='wb') as wb:
        wb.setnchannels(1)  # モノラル
        wb.setsampwidth(2)  # 16bit=2byte
        wb.setframerate(frame_rate)
        wb.writeframes(data.tobytes())  # バイト列に変換
    return data


def save_sound_info(data, name):
    info = data.getparams()
    f = open(name+"_info.txt", 'w')
    params = ['nchannels', 'sampwidth', 'framerate',
              'nframes', 'comptype', 'compname']
    for p, i in zip(params, info):
        print(p, i)
        f.write(p+': '+str(i)+'\n')
    f.close()


def save_sound_wave(data, name):
    buff = data.readframes(-1)
    convert = np.frombuffer(buff, dtype=np.int16)
    if data.getnchannels() == 2:
        convert_l = convert[::2]
        convert_r = convert[1::2]
        plt.subplot(211)
        plt.plot(convert_l)
        plt.subplot(212)
        plt.plot(convert_r)
    else:
        plt.plot(convert)
    plt.savefig(name+"_wave.png")


def save_sound_frequency(data, name):
    buff = data.readframes(-1)
    convert = np.frombuffer(buff, dtype=np.int16)
    fig = plt.figure(figsize=(10, 4))
    spectrum, freqs, t, im = plt.specgram(
        convert, NFFT=512, noverlap=512/16*15, Fs=data.getframerate(), cmap="gray")
    fig.colorbar(im).set_label('Intensity [dB]')
    plt.xlabel('Time [sec]')
    plt.ylabel('Frequency [Hz]')
    plt.savefig('./'+name+'_spectrum.png')
    plt.show()
