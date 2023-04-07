import numpy as np
import matplotlib.pyplot as plt
import simulation
import harvested_energy_estimation

'''
This script simulates the performance of the ThermoBeat system under varying ambient temperatures and temperature gradients, using the teg_output and ltc3108_output functions from the simulation module, as well as the energy_harvested function from the harvested energy estimation module.

The script generates a heatmap, showing the harvested energy as a function of ambient temperature and temperature gradient. This visualization can help identify the optimal operating conditions for the ThermoBeat system.

To generate the heatmap, execute the following command from the software/ambient_conditions folder:
python ambient_conditions_simulation.py

A window with the heatmap should appear, showing the relationship between harvested energy and the input parameters of ambient temperature and temperature gradient.
'''


def simulate_ambient_conditions(ambient_temperatures, temperature_gradient_range, duration):
    energies = []

    for ambient_temperature in ambient_temperatures:
        temp_energies = []

        for temperature_gradient in temperature_gradient_range:
            output_voltage, output_current = simulation.teg_output(temperature_gradient, 50.4, 3.11)
            output_voltage, output_current = simulation.ltc3108_output(output_voltage, output_current)

            energy = harvested_energy_estimation.energy_harvested(temperature_gradient, duration, output_voltage, output_current)
            temp_energies.append(energy)

        energies.append(temp_energies)

    return np.array(energies)

def plot_ambient_conditions_simulation(ambient_temperatures, temperature_gradient_range, energies):
    fig, ax = plt.subplots()

    cax = ax.imshow(energies, cmap='viridis', extent=[temperature_gradient_range[0], temperature_gradient_range[-1], ambient_temperatures[0], ambient_temperatures[-1]], origin='lower', aspect='auto')

    ax.set_xlabel("Temperature Gradient (°C)")
    ax.set_ylabel("Ambient Temperature (°C)")
    ax.set_title("Energy Harvested vs. Ambient Temperature and Temperature Gradient")
    cbar = fig.colorbar(cax, ax=ax)
    cbar.set_label("Harvested Energy (mWh)")

    plt.show()

if __name__ == "__main__":
    ambient_temperatures = np.linspace(20, 40, 21)
    temperature_gradient_range = np.linspace(1, 10, 10)
    duration = 8.0

    energies = simulate_ambient_conditions(ambient_temperatures, temperature_gradient_range, duration)
    plot_ambient_conditions_simulation(ambient_temperatures, temperature_gradient_range, energies)
