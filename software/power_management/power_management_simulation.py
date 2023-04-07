import numpy as np
import matplotlib.pyplot as plt
import simulation
import harvested_energy_estimation

'''
This script simulates the power management system for a rechargeable 1200 mAh battery integrated with the ThermoBeat system, considering factors such as temperature gradient, battery voltage, and device power consumption. It uses the teg_output and ltc3108_output functions from the simulation module, as well as the energy_harvested function from the harvested energy estimation module.

The script generates a plot showing the battery energy level over time under the specified conditions.

To generate the plot, execute the following command from the software/power_management folder:
python power_management_simulation.py

A window with the plot should appear, showing the battery energy level over time under the specified conditions, such as temperature gradient, battery capacity, and device power consumption.
'''

def simulate_power_management(temperature_gradient, battery_capacity_mAh, battery_voltage, device_power_consumption_mW, simulation_duration_hours):
    output_voltage, output_current = simulation.teg_output(temperature_gradient, 50.4, 3.11)
    output_voltage, output_current = simulation.ltc3108_output(output_voltage, output_current)

    battery_energy_capacity_mWh = battery_capacity_mAh * battery_voltage
    energy_harvested_per_hour_mWh = harvested_energy_estimation.energy_harvested(temperature_gradient, 1, output_voltage, output_current)
    
    battery_energy_level = battery_energy_capacity_mWh
    battery_energy_levels = [battery_energy_level]

    for _ in range(simulation_duration_hours):
        battery_energy_level += energy_harvested_per_hour_mWh
        battery_energy_level -= device_power_consumption_mW
        battery_energy_level = min(battery_energy_level, battery_energy_capacity_mWh)
        battery_energy_levels.append(battery_energy_level)

    return np.array(battery_energy_levels)

def plot_power_management_simulation(temperature_gradient, battery_capacity_mAh, battery_voltage, device_power_consumption_mW, simulation_duration_hours):
    battery_energy_levels = simulate_power_management(temperature_gradient, battery_capacity_mAh, battery_voltage, device_power_consumption_mW, simulation_duration_hours)

    plt.plot(range(simulation_duration_hours + 1), battery_energy_levels)
    plt.xlabel("Time (hours)")
    plt.ylabel("Battery Energy Level (mWh)")
    plt.title(f"Power Management Simulation ({temperature_gradient} °C gradient, {battery_capacity_mAh} mAh battery)")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    temperature_gradient = 3
    battery_capacity_mAh = 1200
    battery_voltage = 3.7
    device_power_consumption_mW = 336
    simulation_duration_hours = 72

    plot_power_management_simulation(temperature_gradient, battery_capacity_mAh, battery_voltage, device_power_consumption_mW, simulation_duration_hours)
