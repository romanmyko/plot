import matplotlib.pyplot as plt
import math

x_vals = []
y_vals = []

amplitude = 1  # V
frequency = 50  # Hz
time_duration = 0.1  # s
sampling_rate = 100  # 

for it in range(0, int(sampling_rate ), 1):
    x_vals.append(int(it))

for it_y in x_vals:
    y_vals.append( amplitude * math.sin(2 * math.pi * frequency * it_y / 1000))

plt.plot(x_vals, y_vals)
plt.ylabel('sin(x)')
plt.title('')
plt.grid(True)
plt.show()
