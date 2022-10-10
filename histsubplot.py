import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0, 1.0, 100000)

#plt.plot(x)
# matplotlib is indexed from 1, not 0
plt.subplot(1, 2, 1) # num columns, num rows, index of plot position on grid
plt.hist(x, bins=80, label='Normal')
plt.xlabel("Values1") # Always put in units
plt.ylabel("Frequency1")
plt.legend()

x = np.random.uniform(-4.0, 3.0, 1000)
plt.subplot(1, 2, 2) # Put this plot in the second space
plt.hist(x, label='Uniform')
plt.xlabel("Values2") # Always put in units
plt.ylabel("Frequency2")
plt.legend()

plt.title("Normal & Uniform Histogram")
plt.show()