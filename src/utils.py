import numpy as np
import matplotlib.pyplot as plt
import wave as wave
import sounddevice as sd
import logging
import os


def play_sound(data, frame_rate):
    sd.play(data, frame_rate)
    print("Play sound...")
    status = sd.wait()


def record_sound(second_length,frame_rate):
    print("Record...")
    data=sd.rec(int(second_length*frame_rate), frame_rate,channels=1)
    sd.wait()
    print("Complete")
    return data

def save_sound_info(data,name):
    info=data.getparams()
    f=open(name+"_info.txt",'w')
    params=['nchannels', 'sampwidth', 'framerate', 'nframes', 'comptype', 'compname']
    for p,i in zip(params,info):
        print(p,i)
        f.write(p+': '+str(i)+'\n')
    f.close()

def save_sound_wave(data,name):
    buff=data.readframes(-1)
    convert=np.frombuffer(buff,dtype=np.int16)
    if data.getnchannels()==2:
        convert_l=convert[::2]
        convert_r=convert[1::2]
        plt.subplot(211)
        plt.plot(convert_l)
        plt.subplot(212)
        plt.plot(convert_r)
    else:
        plt.plot(convert)
    plt.savefig(name+"_wave.png")