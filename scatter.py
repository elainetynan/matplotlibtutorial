import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.uniform(0.0, 10.0, 100)
x2 = np.random.uniform(0.0, 5.0, 100)
x3 = np.random.randint(0, 20, 100) # colour must be a random integer
x4 = np.random.normal(0.0, 10.0, 100)

#4D graph
plt.scatter(x1, x2, c=x3, s=x4) # c = colour, s = size

plt.xlabel("Values1") # Always put in units
plt.ylabel("Values2")
plt.legend()

plt.title("Scatter Plot")
plt.show()