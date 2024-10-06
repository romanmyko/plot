from signalType import Signal
import matplotlib.pyplot as plt

x = Signal()
d = x.sinus_wave()

plt.plot(d[1], d[2])
plt.ylabel('sin(x)')
plt.title('Графік синусоїди')
plt.grid(True)
plt.show()