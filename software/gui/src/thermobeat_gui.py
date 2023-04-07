import tkinter as tk
from tkinter import ttk
import simulation
import harvested_energy_estimation

class ThermoBeatGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ThermoBeat GUI")
        self.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        self.label_temperature_gradient = ttk.Label(self, text="Temperature Gradient (°C):")
        self.label_temperature_gradient.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)

        self.entry_temperature_gradient = ttk.Entry(self)
        self.entry_temperature_gradient.grid(column=1, row=0, padx=10, pady=10)

        self.label_duration = ttk.Label(self, text="Duration (hours):")
        self.label_duration.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)

        self.entry_duration = ttk.Entry(self)
        self.entry_duration.grid(column=1, row=1, padx=10, pady=10)

        self.button_simulate = ttk.Button(self, text="Simulate", command=self.simulate)
        self.button_simulate.grid(column=0, row=2, padx=10, pady=10)

        self.button_estimate_energy = ttk.Button(self, text="Estimate Harvested Energy", command=self.estimate_energy)
        self.button_estimate_energy.grid(column=1, row=2, padx=10, pady=10)

    def simulate(self):
        temperature_gradient = float(self.entry_temperature_gradient.get())
        duration = float(self.entry_duration.get())

        output_voltage, output_current = simulation.teg_output(temperature_gradient, 50.4, 3.11)
        output_voltage, output_current = simulation.ltc3108_output(output_voltage, output_current)

        print(f"Output Voltage: {output_voltage} mV")
        print(f"Output Current: {output_current} mA")

    def estimate_energy(self):
        temperature_gradient = float(self.entry_temperature_gradient.get())
        duration = float(self.entry_duration.get())

        output_voltage, output_current = simulation.teg_output(temperature_gradient, 50.4, 3.11)
        output_voltage, output_current = simulation.ltc3108_output(output_voltage, output_current)

        energy = harvested_energy_estimation.energy_harvested(temperature_gradient, duration, output_voltage, output_current)
        print(f"Harvested Energy: {energy} mWh")

if __name__ == "__main__":
    app = ThermoBeatGUI()
    app.mainloop()
