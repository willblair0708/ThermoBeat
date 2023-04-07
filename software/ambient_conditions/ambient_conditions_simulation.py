import numpy as np
import matplotlib.pyplot as plt
import simulation
import harvested_energy_estimation

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
