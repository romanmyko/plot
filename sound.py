import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

frequency = 500  # Hz 
amplitude = 0.5  # amplitude 0-1
duration = 2.0   # time - s
sampling_rate = 44100  

def plot_graf(x, y, frequency):
    plt.plot(x, y)
    plt.xlabel(f't,s,{frequency} hz')
    plt.ylabel(f'amplitude')
    plt.title('')
    plt.grid(True)
    plt.show()

t = np.linspace(0, duration, int(sampling_rate ), endpoint=False)
y = amplitude * np.sin(2 * np.pi * frequency * t)
sd.play(y, samplerate=sampling_rate)
sd.wait()  

graf_divider = int(sampling_rate / 100)
plot_graf(t[:graf_divider], y[:graf_divider], frequency)


