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
   
