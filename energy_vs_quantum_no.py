import numpy as np
import matplotlib.pyplot as plt

# Constants
h_bar = 1.0545718e-34  # Reduced Planck constant (J·s)
m_e = 9.10938356e-31   # Electron mass (kg)
L = 1e-9               # Size of the nanomaterial (1 nm = 1e-9 m)

# Quantum numbers for energy levels (E_n vs. n)
n_values = np.arange(1, 21)  # Quantum numbers from 1 to 20

# Function to calculate energy levels for a particle in a box
def energy_level(n):
    return (n**2 * np.pi**2 * h_bar**2) / (2 * m_e * L**2)

# Get energy levels for each quantum number n
energies_n = energy_level(n_values)

# Plot Energy Levels (En) vs Quantum Number (n)
plt.figure(figsize=(8, 6))
plt.plot(n_values, energies_n, 'o-', color='green', label=r'$E_n$ vs. $n$')
plt.xlabel("Quantum Number (n)")
plt.ylabel("Energy Levels (Joules)")
plt.title("Energy Levels (En) vs. Quantum Number (n)")
plt.legend()
plt.grid(True)
plt.xticks(n_values)
plt.show()
