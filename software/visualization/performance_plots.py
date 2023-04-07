import numpy as np
import matplotlib.pyplot as plt
import simulation
import harvested_energy_estimation

'''
This script generates two plots:

The first plot shows the relationship between TEG output voltage and output current with respect to the temperature gradient. It uses the teg_output function from the simulation module to calculate output voltage and output current for a range of temperature gradients.

The second plot shows the relationship between harvested energy and duration, assuming a constant temperature gradient. It uses the energy_harvested function from the harvested energy estimation module to calculate the energy harvested for a range of durations.

To generate the plots, execute the following command from the software/visualization folder:

python performance_plots.py
Two windows with the performance plots should appear, showing the relationship between TEG output, harvested energy, and the input parameters of temperature gradient and duration.
'''

def plot_teg_output_vs_temperature_gradient():
    temperature_gradients = np.linspace(1, 10, 100)
    output_voltages = []
    output_currents = []

    for temperature_gradient in temperature_gradients:
        output_voltage, output_current = simulation.teg_output(temperature_gradient, 50.4, 3.11)
        output_voltages.append(output_voltage)
        output_currents.append(output_current)

    plt.plot(temperature_gradients, output_voltages, label="Output Voltage (mV)")
    plt.plot(temperature_gradients, output_currents, label="Output Current (mA)")
    plt.xlabel("Temperature Gradient (°C)")
    plt.ylabel("Output Voltage (mV) / Output Current (mA)")
    plt.title("TEG Output vs. Temperature Gradient")
    plt.legend()
    plt.grid()
    plt.show()

def plot_energy_harvested_vs_duration():
    temperature_gradient = 3.0
    durations = np.linspace(1, 10, 100)
    energies = []

    output_voltage, output_current = simulation.teg_output(temperature_gradient, 50.4, 3.11)
    output_voltage, output_current = simulation.ltc3108_output(output_voltage, output_current)

    for duration in durations:
        energy = harvested_energy_estimation.energy_harvested(temperature_gradient, duration, output_voltage, output_current)
        energies.append(energy)

    plt.plot(durations, energies)
    plt.xlabel("Duration (hours)")
    plt.ylabel("Harvested Energy (mWh)")
    plt.title("Energy Harvested vs. Duration")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_teg_output_vs_temperature_gradient()
    plot_energy_harvested_vs_duration()
