import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01) # arange is for decimal numbers
y = 3.0 * x
noise = np.random.normal(0.0, 1.0, len(x))

# By having the Fitted model second it goes on the top
#plt.plot(x, noise, 'g-') # green line only
plt.plot(x, y+noise, 'g.', label = 'Actual Data') # add noise to y
plt.plot(x, y, 'b-', label='Fitted Model', linewidth=5.0) # blue points only

plt.title("Average Speed v Distance Covered")
plt.xlabel("Average Speed (km/h)") # Always put in units
plt.ylabel("Distance Covered (km)")
plt.legend()

plt.show()