import numpy as np
import matplotlib.pyplot as plt

# Constants
h_bar = 1.0545718e-34  # Reduced Planck constant (J·s)
m_e = 9.10938356e-31   # Electron mass (kg)
L = 1e-9               # Size of the nanomaterial (1 nm = 1e-9 m)
num_k = 500            # Number of k-points for DOS calculation

# Function to calculate energy for a free electron model
def energy(k):
    return (h_bar**2 * k**2) / (2 * m_e)

# Generate k-points and calculate energies for DOS
k_values = np.linspace(0, np.pi / L, num_k)
energies = energy(k_values)

# Function to calculate DOS
def calculate_dos(energies, num_bins=100):
    hist, bin_edges = np.histogram(energies, bins=num_bins, density=True)
    dos = hist / np.diff(bin_edges)
    energy_centers = (bin_edges[1:] + bin_edges[:-1]) / 2  # Midpoints of bins
    return energy_centers, dos

# Calculate DOS for the generated energies
energy_centers, dos = calculate_dos(energies)

# Quantum numbers for energy levels (E_n vs. n)
n_values = np.arange(1, 21)  # Quantum numbers from 1 to 20

# Function to calculate energy levels for a particle in a box
def energy_level(n):
    return (n**2 * np.pi**2 * h_bar**2) / (2 * m_e * L**2)

# Get energy levels for each quantum number n
energies_n = energy_level(n_values)

# Plotting both DOS and E_n vs n
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot Density of States (DOS)
axs[0].plot(energy_centers, dos, color='blue', label='Density of States (DOS)')
axs[0].set_xlabel("Energy (Joules)")
axs[0].set_ylabel("Density of States (DOS)")
axs[0].set_title("Density of States for a Free Electron Model")
axs[0].legend()
axs[0].grid(True)

# Plot Energy Levels (En) vs Quantum Number (n)
axs[1].plot(n_values, energies_n, 'o-', color='green', label=r'$E_n$ vs. $n$')
axs[1].set_xlabel("Quantum Number (n)")
axs[1].set_ylabel("Energy Levels (Joules)")
axs[1].set_title("Energy Levels (En) vs. Quantum Number (n)")
axs[1].legend()
axs[1].grid(True)
axs[1].set_xticks(n_values)
plt.tight_layout()
plt.show()
