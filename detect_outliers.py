import numpy as np
import pandas as pd
from scipy import stats

# Method 1: Z-score method


def detect_outliers_zscore(data, threshold=3):
    z_scores = np.abs(stats.zscore(data))
    outliers = np.where(z_scores > threshold)[0]
    return outliers

# Method 2: IQR method


def detect_outliers_iqr(data, k=1.5):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr
    outliers = np.where((data < lower_bound) | (data > upper_bound))[0]
    return outliers

# Method 3: Tukey's fences method


def detect_outliers_tukey(data, k=1.5):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr
    outliers = np.where((data < lower_bound) | (data > upper_bound))[0]
    return outliers


# Example usage
dataset = pd.read_csv('your_dataset.csv')
column_name = 'your_column'

# Detect outliers using Z-score method
outliers_zscore = detect_outliers_zscore(dataset[column_name])

# Detect outliers using IQR method
outliers_iqr = detect_outliers_iqr(dataset[column_name])

# Detect outliers using Tukey's fences method
outliers_tukey = detect_outliers_tukey(dataset[column_name])

# Print the detected outliers
print("Outliers (Z-score method):", outliers_zscore)
print("Outliers (IQR method):", outliers_iqr)
print("Outliers (Tukey's fences method):", outliers_tukey)
