import numpy as np
import matplotlib.pyplot as plt
import math

e0 = 50
pi = math.pi
amplitude = 220

t = np.linspace(0, 100)
fase0 = 2 * math.pi * t * amplitude


y0 = e0 * np.cos(fase0)
y1 = e0 * np.cos(fase0 + 2 * pi / 3)
y2 = e0 * np.cos(fase0 + 4 * pi / 3)


y3 = [0] * len(t)


plt.plot(t, y0, label='Фаза 0')
plt.plot(t, y1, label='Фаза 120°')
plt.plot(t, y2, label='Фаза 240°')
plt.plot(t, y3, label='Нульовий рівень', linestyle='--')


plt.xlabel('t')
plt.ylabel('y')
plt.title('Графік синусоїди із трифазним зміщенням')
plt.grid(True)
plt.legend() 

plt.show()
