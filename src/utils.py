import wave as wave
import sounddevice as sd


def play(data, frame_rate):
    sd.play(data, frame_rate)
    print("Play sound...")
    status = sd.wait()
