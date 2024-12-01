
import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 9.11e-31  # Electron mass in kg
hbar = 1.054e-34  # Reduced Planck's constant in J.s

# Energy range (in Joules)
E = np.linspace(1e-21, 1e-18, 1000)  # Avoid E = 0 to prevent division by zero

# DOS formulas
g_1D = (1 / np.sqrt(E)) * (m / hbar**2)
g_2D = m / (np.pi * hbar**2) * np.ones_like(E)  # Constant w.r.t E
g_3D = 0.5 * ((2 * m / hbar**2)**1.5) * np.sqrt(E)

# Plotting with linear scales
plt.figure(figsize=(10, 6))
plt.plot(E, g_1D, label="1D DOS", color="blue")
plt.plot(E, g_2D, label="2D DOS", color="green")
plt.plot(E, g_3D, label="3D DOS", color="red")

plt.xlabel("Energy (E) [J]")
plt.ylabel("Density of States g(E) [arbitrary units]")
plt.title("Density of States vs Energy for 1D, 2D, and 3D Systems (Linear Scale)")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()