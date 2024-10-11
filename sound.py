import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import sys
import os
import time

frequency = 9000  # Hz
amplitude = 0.5  # amplitude 0-1
duration = 0.001   # time - s
sampling_rate = 44100
rate = 100


def plot_graf(x, y, frequency):
    plt.plot(x, y)
    plt.xlabel(f't,s,{frequency} hz')
    plt.ylabel(f'amplitude')
    plt.title('')
    plt.grid(True)
    plt.show()
    time.sleep(1)
    plt.close()


def set_duration(frequency):
    if frequency <= 1000:
        duration = 1
    elif 1000 < frequency <= 10000:
        duration = 0.1
    elif 10000 < frequency <= 44000:
        duration = 0.01
    else:
        duration = 0.001
    return duration


while True:
    try:
        frequency = int(input('Input frequency: '))
        os.system('clear')
    except ValueError:
        print("Please enter a valid integer for frequency.")
        sys.exit()


    t = np.linspace(0, set_duration(frequency), int(sampling_rate), endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    sd.play(y, samplerate=sampling_rate)
    sd.wait()

    graf_divider = int(sampling_rate / rate)
    plot_graf(t[:graf_divider], y[:graf_divider], frequency)
    print("Exit type str")
