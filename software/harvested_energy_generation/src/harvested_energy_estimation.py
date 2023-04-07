import numpy as np
import matplotlib.pyplot as plt

def energy_harvested(temperature_gradient, duration, output_voltage, output_current):
    """
    Calculate the energy harvested by the ThermoBeat system for a given temperature gradient and duration.

    Args:
    temperature_gradient (float): The temperature gradient across the TEG module (in °C).
    duration (float): The duration of energy harvesting (in hours).
    output_voltage (float): The output voltage of the LTC3108 boost converter (in mV).
    output_current (float): The output current of the LTC3108 boost converter (in mA).

    Returns:
    float: The energy harvested by the ThermoBeat system for the given temperature gradient and duration (in mWh).
    """
    output_power = output_voltage * output_current  # mW
    energy = output_power * duration  # mWh

    return energy

def plot_energy_harvested(temperature_gradients, harvested_energy):
    """
    Plot the energy harvested by the ThermoBeat system vs. temperature gradient.

    Args:
    temperature_gradients (np.ndarray): An array containing the temperature gradient values.
    harvested_energy (np.ndarray): An array containing the energy harvested values for each temperature gradient.
    """
    plt.figure()
    plt.plot(temperature_gradients, harvested_energy, label='Harvested Energy')
    plt.xlabel('Temperature Gradient (°C)')
    plt.ylabel('Harvested Energy (mWh)')
    plt.legend()
    plt.title('Harvested Energy vs. Temperature Gradient')

def main():
    # Use the simulation results obtained in the previous script
    temperature_gradients = np.linspace(1, 5, 50)  # An array of temperature gradients from 1°C to 5°C
    output_voltages = [3300] * len(temperature_gradients)  # Assume a constant output voltage of 3300 mV
    output_currents = [0.1, 0.15, 0.2, 0.25, 0.3]  # Example output currents in mA

    durations = [1, 2, 4, 8, 12]  # Example durations in hours

    for i, duration in enumerate(durations):
        harvested_energy = np.array([energy_harvested(gradient, duration, output_voltages[i], output_currents[i]) for gradient in temperature_gradients])
        plot_energy_harvested(temperature_gradients, harvested_energy)

    plt.show()

if __name__ == "__main__":
    main()

