import numpy as np


class Signal:
    """
    Class for representing a variable sinusoidal voltage.

    Attributes:
    ----------
    amplitude : float
        The amplitude of the signal in Volts.
    frequency : float
        The frequency of the signal in Hertz.
    time : float
        The time over which the signal is generated, in seconds.
    sampling_rate: int
        The sampling rate, in point
    Methods:
    -------
    sinus_wave():
        Generates a sinusoidal wave based on the current signal parameters.
    """

    def __init__(self, amplitude=220, frequency=50, time_duration=0.1, sampling_rate=10000) -> None:
        self.amplitude = amplitude
        self.frequency = frequency
        self.time_duration = time_duration
        self.sampling_rate = sampling_rate

    def sinus_wave(self):
        t = np.linspace(0, self.time_duration, int(
            self.time_duration * self.sampling_rate))
        x_vals = t
        y_vals = self.amplitude * np.sin(2 * np.pi * self.frequency * t)

        return f" frequency: {self.frequency} Hz , '/n' amplitude {self.amplitude} V ", x_vals, y_vals
