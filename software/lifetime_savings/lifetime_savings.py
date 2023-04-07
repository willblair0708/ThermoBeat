import numpy as np
import matplotlib.pyplot as plt
import simulation
import harvested_energy_estimation

'''
This script calculates the lifetime energy savings of the ThermoBeat system, considering factors such as battery capacity, battery degradation rate, and device power consumption. It uses the teg_output and ltc3108_output functions from the simulation module, as well as the energy_harvested function from the harvested energy estimation module.

The script generates a plot showing the lifetime energy savings for a range of battery capacities, given a specific temperature gradient and duration in years.

To generate the plot, execute the following command from the software/lifetime_savings folder:

python lifetime_savings.py
A window with the plot should appear, showing the relationship between lifetime energy savings and the input parameters of battery capacity, temperature gradient, and duration in years.
'''

def calculate_lifetime_savings(temperature_gradient, battery_capacity, battery_degradation_rate, device_power_consumption, duration_years):
    output_voltage, output_current = simulation.teg_output(temperature_gradient, 50.4, 3.11)
    output_voltage, output_current = simulation.ltc3108_output(output_voltage, output_current)

    energy_harvested_per_year = 365 * 24 * harvested_energy_estimation.energy_harvested(temperature_gradient, 1, output_voltage, output_current)
    battery_energy_capacity = battery_capacity * 365 * 24

    battery_remaining_capacity = battery_energy_capacity
    teg_total_energy_produced = 0

    for year in range(duration_years):
        battery_remaining_capacity -= device_power_consumption * 365 * 24
        battery_remaining_capacity *= (1 - battery_degradation_rate)
        teg_total_energy_produced += energy_harvested_per_year

    return teg_total_energy_produced, battery_remaining_capacity

def plot_lifetime_savings(duration_years, temperature_gradient):
    battery_capacities = np.linspace(1000, 10000, 10)
    teg_energy_savings = []

    for battery_capacity in battery_capacities:
        teg_energy, battery_energy = calculate_lifetime_savings(temperature_gradient, battery_capacity, 0.02, 336, duration_years)
        energy_savings = teg_energy - battery_energy
        teg_energy_savings.append(energy_savings)

    plt.plot(battery_capacities, teg_energy_savings)
    plt.xlabel("Battery Capacity (mWh)")
    plt.ylabel("Lifetime Energy Savings (mWh)")
    plt.title(f"Lifetime Energy Savings with ThermoBeat ({duration_years} years, {temperature_gradient} °C gradient)")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    duration_years = 10
    temperature_gradient = 3

    plot_lifetime_savings(duration_years, temperature_gradient)
