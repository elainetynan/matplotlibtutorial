import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.0, 15.0, 0.1) # arange is for decimal numbers

plt.plot(x, x**2, 'g-', label = 'x^2', linewidth=1.5)
plt.plot(x, x**3, 'b-', label = 'x^3', linewidth=1.5)
plt.plot(x, x**4, 'r-', label = 'x^4', linewidth=1.5)
plt.plot(x, 2**x, 'k-', label = '2^x', linewidth=1.5)

plt.title("Powers")
plt.xlabel("Val1") # Always put in units
plt.ylabel("Val2)")
plt.legend()

plt.show()