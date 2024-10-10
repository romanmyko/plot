from signalType import Signal
import matplotlib.pyplot as plt
import sounddevice as sd

data = [0.5, 440 , 1, 1000] # V, Hz, duration-s , t-s 
signal_in = Signal(amplitude=data[0], frequency=data[1], time_duration=data[2], sampling_rate=data[3])
sin_out = signal_in.sinus_wave()
meandr_out = signal_in.meandr_wave()

plt.plot(sin_out[1], sin_out[2])
plt.plot(meandr_out[1], meandr_out[2])

plt.xlabel('t,s')
plt.ylabel('v,V')
plt.title('')
plt.grid(True)
plt.show()

sd.play(sin_out[1], sin_out[2])
sd.wait()  
