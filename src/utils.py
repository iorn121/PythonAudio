import wave as wave
import sounddevice as sd


def play(data, frame_rate):
    sd.play(data, frame_rate)
    print("Play sound...")
    status = sd.wait()


def record(secoond_length,frame_rate):
    print("Record...")
    data=sd.rec(int(secoond_length*frame_rate), frame_rate,channels=1)
    sd.wait()
    print("Complete")
    return data

frame_rate=16000
data=record(3,frame_rate)

play(data, frame_rate)