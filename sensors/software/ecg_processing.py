import numpy as np
import pandas as pd
import scipy.signal as signal

def read_ecg_data(file_path):
    ecg_data = pd.read_csv(file_path)
    return ecg_data

def preprocess_ecg(ecg_data, sample_rate):
    nyquist_freq = 0.5 * sample_rate
    low = 0.5 / nyquist_freq
    high = 50 / nyquist_freq

    b, a = signal.butter(1, [low, high], btype='band')
    filtered_ecg = signal.lfilter(b, a, ecg_data)

    return filtered_ecg

def detect_qrs(filtered_ecg, sample_rate):
    qrs_indices = signal.qrs_detect(filtered_ecg, sample_rate)
    return qrs_indices

def calculate_hrv(qrs_indices):
    rr_intervals = np.diff(qrs_indices)
    hrv_metrics = {
        'mean_rr': np.mean(rr_intervals),
        'sdnn': np.std(rr_intervals),
        'rmssd': np.sqrt(np.mean(np.square(np.diff(rr_intervals))))
    }

    return hrv_metrics

if __name__ == "__main__":
    file_path = '../data/example_ecg_data.csv'
    sample_rate = 1000

    ecg_data = read_ecg_data(file_path)
    filtered_ecg = preprocess_ecg(ecg_data, sample_rate)
    qrs_indices = detect_qrs(filtered_ecg, sample_rate)
    hrv_metrics = calculate_hrv(qrs_indices)

    print("QRS Indices:", qrs_indices)
    print("HRV Metrics:", hrv_metrics)
