import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2.0 * np.pi, 2.0*np.pi, 0.1) # arange is for decimal numbers

plt.plot(x, np.sin(x), 'g-', label = 'Sin', linewidth=2.0)
plt.plot(x, np.cos(x), 'b.', label = 'Cos')

plt.title("Sin & Cos curve")
plt.xlabel("Val1") # Always put in units
plt.ylabel("Val2)")
plt.legend()

plt.show()