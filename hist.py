import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0, 1.0, 100000)

#plt.plot(x)
plt.hist(x, bins=80, label='Vals')

plt.title("Normal Curve Histogram")
plt.xlabel("Values") # Always put in units
plt.ylabel("Frequency")
plt.legend()
plt.show()