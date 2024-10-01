import matplotlib.pyplot as plt
import math

x_vals = []
y_vals = []

for it in range(1000):
    zx = it * 0.4 * 3.14
    zy = math.sin(it)
    x_vals.append(zx)
    y_vals.append(zy)

plt.plot(x_vals, y_vals)
plt.ylabel('sin(x)')
plt.title('Графік синусоїди')
plt.grid(True)
plt.show()
