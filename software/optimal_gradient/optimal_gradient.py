import numpy as np
import matplotlib.pyplot as plt
import simulation
import harvested_energy_estimation

'''
This script calculates the optimal temperature gradient required for different device power consumption scenarios. It uses the teg_output and ltc3108_output functions from the simulation module, as well as the energy_harvested function from the harvested_energy_estimation module.

The script generates a plot showing the relationship between the optimal temperature gradient and device power consumption.

To generate the plot, execute the following command from the software/optimal_gradient folder:
python optimal_gradient.py

A window with the plot should appear, showing the optimal temperature gradient required for different device power consumption scenarios. This information can be useful for determining the minimum temperature gradient needed for the ThermoBeat system to operate efficiently under various conditions.
'''

def find_optimal_gradient(device_power_consumption_mW):
    temperature_gradients = np.linspace(0.5, 10, 100)
    required_gradients = []

    for temperature_gradient in temperature_gradients:
        output_voltage, output_current = simulation.teg_output(temperature_gradient, 50.4, 3.11)
        output_voltage, output_current = simulation.ltc3108_output(output_voltage, output_current)

        harvested_energy_mW = output_voltage * output_current
        if harvested_energy_mW >= device_power_consumption_mW:
            required_gradients.append(temperature_gradient)
            break
    return required_gradients

def plot_optimal_gradient(device_power_consumptions_mW):
    optimal_gradients = []

    for device_power_consumption_mW in device_power_consumptions_mW:
        optimal_gradient = find_optimal_gradient(device_power_consumption_mW)
        optimal_gradients.append(optimal_gradient)

    plt.plot(device_power_consumptions_mW, optimal_gradients)
    plt.xlabel("Device Power Consumption (mW)")
    plt.ylabel("Optimal Temperature Gradient (°C)")
    plt.title("Optimal Temperature Gradient for Different Device Power Consumption Scenarios")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    device_power_consumptions_mW = np.linspace(50, 500, 10)

    plot_optimal_gradient(device_power_consumptions_mW)
