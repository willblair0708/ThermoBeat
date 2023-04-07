import numpy as np
import matplotlib.pyplot as plt

def teg_output(temperature_gradient, open_circuit_voltage_per_gradient, short_circuit_current_per_gradient):
    """
    Calculate the TEG module's output voltage and current for a given temperature gradient.

    Args:
    temperature_gradient (float): The temperature gradient across the TEG module (in °C).
    open_circuit_voltage_per_gradient (float): The open-circuit voltage per degree Celsius of temperature gradient (in mV/°C).
    short_circuit_current_per_gradient (float): The short-circuit current per degree Celsius of temperature gradient (in mA/°C).

    Returns:
    tuple: A tuple containing the output voltage (in mV) and output current (in mA) for the given temperature gradient.
    """
    voltage = open_circuit_voltage_per_gradient * temperature_gradient
    current = short_circuit_current_per_gradient * temperature_gradient

    return voltage, current

def ltc3108_output(input_voltage, input_current):
    """
    Calculate the LTC3108 boost converter's output voltage and current for a given input voltage and current.

    Args:
    input_voltage (float): The input voltage to the LTC3108 boost converter (in mV).
    input_current (float): The input current to the LTC3108 boost converter (in mA).

    Returns:
    tuple: A tuple containing the output voltage (in mV) and output current (in mA) for the given input voltage and current.
    """
    # Constants for LTC
