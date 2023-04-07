import argparse
import simulation
import harvested_energy_estimation

'''
1. Simulate the ThermoBeat system for a 3°C temperature gradient and a 2-hour duration:
python thermobeat_cli.py 3 2 --simulate

2. Estimate the harvested energy for a 3°C temperature gradient and a 2-hour duration:
python thermobeat_cli.py 3 2 --estimate_energy

3. Perform both simulation and energy estimation for a 3°C temperature gradient and a 2-hour duration:
python thermobeat_cli.py 3 2 --simulate --estimate_energy
'''

def main():
    parser = argparse.ArgumentParser(description="ThermoBeat CLI: Interact with ThermoBeat system simulations and harvested energy estimations.")
    parser.add_argument("temperature_gradient", type=float, help="Temperature gradient across the TEG module (in °C).")
    parser.add_argument("duration", type=float, help="Duration of energy harvesting (in hours).")
    parser.add_argument("--simulate", action="store_true", help="Simulate the ThermoBeat system for the given temperature gradient and duration.")
    parser.add_argument("--estimate_energy", action="store_true", help="Estimate the harvested energy for the given temperature gradient and duration.")

    args = parser.parse_args()

    if args.simulate:
        output_voltage, output_current = simulation.teg_output(args.temperature_gradient, 50.4, 3.11)
        output_voltage, output_current = simulation.ltc3108_output(output_voltage, output_current)

        print(f"Output Voltage: {output_voltage} mV")
        print(f"Output Current: {output_current} mA")

    if args.estimate_energy:
        output_voltage, output_current = simulation.teg_output(args.temperature_gradient, 50.4, 3.11)
        output_voltage, output_current = simulation.ltc3108_output(output_voltage, output_current)

        energy = harvested_energy_estimation.energy_harvested(args.temperature_gradient, args.duration, output_voltage, output_current)
        print(f"Harvested Energy: {energy} mWh")

if __name__ == "__main__":
    main()
