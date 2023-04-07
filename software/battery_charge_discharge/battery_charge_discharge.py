import numpy as np
import matplotlib.pyplot as plt
import simulation

'''
This script simulates the charging and discharging cycles of the battery by considering the energy harvested from the TEG and boost converter, as well as the energy consumed by the device. It uses the teg_output and ltc3108_output functions from the simulation module.

The script generates a plot showing the remaining battery energy over time, simulating the charging and discharging cycles of the battery.

To generate the plot, execute the following command from the software/battery_charge_discharge folder:
python battery_charge_discharge.py

A window with the plot should appear, showing the remaining battery energy over time, illustrating the charging and discharging cycles of the battery. This information can be useful for evaluating the system's performance and identifying potential improvements to the energy harvesting and power management strategies.
'''

def simulate_battery_charge_discharge(temperature_gradient, battery_capacity_mAh, battery_voltage, device_power_consumption_mW, simulation_time_hours, time_step_hours):
    battery_energy_capacity_mWh = battery_capacity_mAh * battery_voltage
    battery_energy_remaining_mWh = battery_energy_capacity_mWh

    time_points = np.arange(0, simulation_time_hours, time_step_hours)
    battery_energy_remaining_history = []

    for t in time_points:
        output_voltage, output_current = simulation.teg_output(temperature_gradient, 50.4, 3.11)
        output_voltage, output_current = simulation.ltc3108_output(output_voltage, output_current)

        energy_harvested_mWh = output_voltage * output_current * time_step_hours
        energy_consumed_mWh = device_power_consumption_mW * time_step_hours

        battery_energy_remaining_mWh += energy_harvested_mWh - energy_consumed_mWh
        battery_energy_remaining_mWh = min(battery_energy_remaining_mWh, battery_energy_capacity_mWh)

        battery_energy_remaining_history.append(battery_energy_remaining_mWh)

    return time_points, battery_energy_remaining_history

def plot_battery_charge_discharge(time_points, battery_energy_remaining_history):
    plt.plot(time_points, battery_energy_remaining_history)
    plt.xlabel("Time (hours)")
    plt.ylabel("Remaining Battery Energy (mWh)")
    plt.title("Battery Charge and Discharge Simulation")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    temperature_gradient = 3
    battery_capacity_mAh = 1200
    battery_voltage = 3.7
    device_power_consumption_mW = 336
    simulation_time_hours = 200
    time_step_hours = 0.1

    time_points, battery_energy_remaining_history = simulate_battery_charge_discharge(temperature_gradient, battery_capacity_mAh, battery_voltage, device_power_consumption_mW, simulation_time_hours, time_step_hours)
    plot_battery_charge_discharge(time_points, battery_energy_remaining_history)
