import numpy as np
import matplotlib.pyplot as plt
import simulation
import harvested_energy_estimation

'''
This script calculates the expected battery life for different temperature gradients and battery capacities. It uses the teg_output and ltc3108_output functions from the simulation module, as well as the energy_harvested function from the harvested_energy_estimation module.

The script generates a heatmap plot showing the relationship between the expected battery life, temperature gradients, and battery capacities.

To generate the plot, execute the following command from the software/battery_life_estimation folder:
python battery_life_estimation.py

A window with the heatmap plot should appear, showing the estimated battery life for different temperature gradients and battery capacities. This information can be useful for determining the appropriate battery capacity and temperature gradient requirements to ensure sufficient battery life for the ThermoBeat system under various conditions.
'''

def battery_life_hours(temperature_gradient, battery_capacity_mAh, battery_voltage, device_power_consumption_mW):
    output_voltage, output_current = simulation.teg_output(temperature_gradient, 50.4, 3.11)
    output_voltage, output_current = simulation.ltc3108_output(output_voltage, output_current)

    energy_harvested_per_hour_mWh = harvested_energy_estimation.energy_harvested(temperature_gradient, 1, output_voltage, output_current)
    battery_energy_capacity_mWh = battery_capacity_mAh * battery_voltage

    net_energy_consumption_mWh = device_power_consumption_mW - energy_harvested_per_hour_mWh
    if net_energy_consumption_mWh > 0:
        battery_life_hours = battery_energy_capacity_mWh / net_energy_consumption_mWh
    else:
        battery_life_hours = float("inf")

    return battery_life_hours

def plot_battery_life(temperature_gradients, battery_capacities_mAh, battery_voltage, device_power_consumption_mW):
    battery_life_matrix = np.zeros((len(temperature_gradients), len(battery_capacities_mAh)))

    for i, temperature_gradient in enumerate(temperature_gradients):
        for j, battery_capacity_mAh in enumerate(battery_capacities_mAh):
            battery_life_matrix[i, j] = battery_life_hours(temperature_gradient, battery_capacity_mAh, battery_voltage, device_power_consumption_mW)

    plt.imshow(battery_life_matrix, cmap="viridis", origin="lower", extent=[min(battery_capacities_mAh), max(battery_capacities_mAh), min(temperature_gradients), max(temperature_gradients)], aspect="auto")
    plt.colorbar(label="Battery Life (hours)")
    plt.xlabel("Battery Capacity (mAh)")
    plt.ylabel("Temperature Gradient (°C)")
    plt.title("Estimated Battery Life for Different Temperature Gradients and Battery Capacities")
    plt.grid(visible=False)
    plt.show()

if __name__ == "__main__":
    temperature_gradients = np.linspace(1, 10, 10)
    battery_capacities_mAh = np.linspace(200, 2000, 10)
    battery_voltage = 3.7
    device_power_consumption_mW = 336

    plot_battery_life(temperature_gradients, battery_capacities_mAh, battery_voltage, device_power_consumption_mW)
