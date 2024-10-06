import numpy as np


class Signal:
    def __init__(self, amplitude = 220, frequency = 50, time_duration = 0.1, sampling_rate = 10000) -> None:
        self.amplitude = amplitude
        self.frequency = frequency
        self.time_duration  = time_duration 
        self.sampling_rate = sampling_rate
    
    def sinus_wave (self):
        t = np.linspace(0, self.time_duration, int(self.time_duration * self.sampling_rate) )
        x_vals = t
        y_vals = self.amplitude * np.sin(2 * np.pi * self.frequency * t)
        
        return f" frequency: {self.frequency} Hz , '/n' amplitude {self.amplitude} V ", x_vals , y_vals
    
# fase0 = 2 * pi * t * frequency
# y0 = amplitude * np.cos(fase0)