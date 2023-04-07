import numpy as np
import matplotlib.pyplot as plt

def teg_output(temperature_gradient):
    """
    Calculate the output voltage and current of the TEG module for a given temperature gradient.

    Args:
    temperature_gradient (float): The temperature gradient across the TEG module in degrees Celsius.

    Returns:
    (float, float): A tuple containing the output voltage (mV) and current (mA) of the TEG module.
    """
    # Constants obtained from TEG specifications
    open_circuit_voltage_per_deg = 50.4 / 3  # mV/°C
    short_circuit_current_per_deg = 3.11 / 3  # mA/°C

    voltage = open_circuit_voltage_per_deg * temperature_gradient
    current = short_circuit_current_per_deg * temperature_gradient

    return voltage, current

def boost_converter_output(teg_voltage, teg_current):
    """
    Calculate the output voltage and current of the LTC3108 boost converter for a given input voltage and current.

    Args:
    teg_voltage (float): The input voltage from the TEG module in mV.
    teg_current (float): The input current from the TEG module in mA.

    Returns:
    (float, float): A tuple containing the output voltage (V) and current (mA) of the LTC3108 boost converter.
    """
    # Constants obtained from LTC3108 specifications
    output_voltage = 3.3  # V
    conversion_efficiency = 0.8

    input_power = teg_voltage * teg_current  # mW
    output_power = input_power * conversion_efficiency  # mW

    output_current = output_power / output_voltage  # mA

    return output_voltage, output_current

def main():
    temperature_gradients = np.linspace(1, 10, 10)  # 1 to 10 degrees Celsius

    teg_voltages = []
    teg_currents = []
    boost_output_voltages = []
    boost_output_currents = []

    for gradient in temperature_gradients:
        teg_voltage, teg_current = teg_output(gradient)
        teg_voltages.append(teg_voltage)
        teg_currents.append(teg_current)

        output_voltage, output_current = boost_converter_output(teg_voltage, teg_current)
        boost_output_voltages.append(output_voltage)
        boost_output_currents.append(output_current)

    plt.figure()
    plt.plot(temperature_gradients, teg_voltages, label='TEG Voltage (mV)')
    plt.plot(temperature_gradients, teg_currents, label='TEG Current (mA)')
    plt.xlabel('Temperature Gradient (°C)')
    plt.ylabel('Output')
    plt.legend()
    plt.title('TEG Module Output vs. Temperature Gradient')

    plt.figure()
    plt.plot(temperature_gradients, boost_output_currents, label='Boost Converter Output Current (mA)')
    plt.xlabel('Temperature Gradient (°C)')
    plt.ylabel('Output Current (mA)')
    plt.legend()
    plt.title('Boost Converter Output Current vs. Temperature Gradient')

    plt.show()

if __name__ == "__main__":
    main()
