import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load experimental data from a CSV file.

    Args:
    file_path (str): The path to the CSV file containing the experimental data.

    Returns:
    pd.DataFrame: A DataFrame containing the experimental data.
    """
    data = pd.read_csv(file_path)
    return data

def calculate_efficiency(data):
    """
    Calculate the overall efficiency of the system for each temperature gradient.

    Args:
    data (pd.DataFrame): A DataFrame containing the experimental data.

    Returns:
    np.ndarray: An array containing the efficiency values for each temperature gradient.
    """
    input_power = data['TEG_Voltage'] * data['TEG_Current']  # mW
    output_power = data['Boost_Converter_Output_Voltage'] * data['Boost_Converter_Output_Current']  # mW

    efficiency = output_power / input_power

    return efficiency

def plot_efficiency(temperature_gradients, efficiency):
    """
    Plot the overall efficiency of the system vs. temperature gradient.

    Args:
    temperature_gradients (np.ndarray): An array containing the temperature gradient values.
    efficiency (np.ndarray): An array containing the efficiency values for each temperature gradient.
    """
    plt.figure()
    plt.plot(temperature_gradients, efficiency, label='Overall Efficiency')
    plt.xlabel('Temperature Gradient (°C)')
    plt.ylabel('Efficiency')
    plt.legend()
    plt.title('Overall Efficiency vs. Temperature Gradient')

def main():
    data_file_path = '../data/experimental_data.csv'  # Update this path with the correct location of your data file

    data = load_data(data_file_path)
    temperature_gradients = data['Temperature_Gradient']
    efficiency = calculate_efficiency(data)

    plot_efficiency(temperature_gradients, efficiency)
    plt.show()

if __name__ == "__main__":
    main()
