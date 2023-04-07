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

def plot_teg_data(data):
    """
    Plot TEG module output voltage and current vs. temperature gradient.

    Args:
    data (pd.DataFrame): A DataFrame containing the experimental data.
    """
    plt.figure()
    plt.plot(data['Temperature_Gradient'], data['TEG_Voltage'], label='TEG Voltage (mV)')
    plt.plot(data['Temperature_Gradient'], data['TEG_Current'], label='TEG Current (mA)')
    plt.xlabel('Temperature Gradient (°C)')
    plt.ylabel('Output')
    plt.legend()
    plt.title('TEG Module Output vs. Temperature Gradient')

def plot_boost_converter_data(data):
    """
    Plot LTC3108 boost converter output voltage and current vs. temperature gradient.

    Args:
    data (pd.DataFrame): A DataFrame containing the experimental data.
    """
    plt.figure()
    plt.plot(data['Temperature_Gradient'], data['Boost_Converter_Output_Current'], label='Boost Converter Output Current (mA)')
    plt.xlabel('Temperature Gradient (°C)')
    plt.ylabel('Output Current (mA)')
    plt.legend()
    plt.title('Boost Converter Output Current vs. Temperature Gradient')

def main():
    data_file_path = '../data/experimental_data.csv'  # Update this path with the correct location of your data file

    data = load_data(data_file_path)

    plot_teg_data(data)
    plot_boost_converter_data(data)

    plt.show()

if __name__ == "__main__":
    main()
   
