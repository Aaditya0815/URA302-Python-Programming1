# Project 1: Sensor Data Analysis
# URA302 - Python Programming Mini Project

import numpy as np
import pandas as pd

# Load sensor data from CSV file
print("Loading sensor data...")
a = pd.read_csv('sensor_data.csv')

# Convert to numpy arrays for calculations
b = a['temperature'].values
c = a['distance'].values
d = a['battery'].values
e = a['humidity'].values
f = a['_datatimestamp'].values

print("Sensor Data Analysis Results:")
print("=" * 40)

# Calculate average, minimum, and maximum for each sensor
print("\n1. STATISTICS FOR EACH SENSOR:")
print("-" * 30)

# Temperature statistics
g = np.mean(b)
h = np.min(b)
i = np.max(b)
print(f"Temperature - Average: {g:.2f}, Min: {h:.2f}, Max: {i:.2f}")

# Distance statistics
j = np.mean(c)
k = np.min(c)
l = np.max(c)
print(f"Distance - Average: {j:.2f}, Min: {k:.2f}, Max: {l:.2f}")

# Battery statistics
m = np.mean(d)
n = np.min(d)
o = np.max(d)
print(f"Battery - Average: {m:.2f}, Min: {n:.2f}, Max: {o:.2f}")

# Humidity statistics
p = np.mean(e)
q = np.min(e)
r = np.max(e)
print(f"Humidity - Average: {p:.2f}, Min: {q:.2f}, Max: {r:.2f}")

# Find time when temperature was highest
print("\n2. TIME WHEN TEMPERATURE WAS HIGHEST:")
print("-" * 35)
s = np.argmax(b)  # Index of maximum temperature
t = f[s]  # Corresponding timestamp
print(f"Highest temperature: {i:.2f}°C")
print(f"Time: {t}")

# Count number of times battery dropped below 30%
print("\n3. BATTERY LOW COUNT:")
print("-" * 20)
u = np.sum(d < 30)  # Count values below 30
print(f"Number of times battery dropped below 30%: {u}")

# Save results to output file
print("\n4. SAVING RESULTS:")
print("-" * 18)
v = {
    'Sensor': ['Temperature', 'Distance', 'Battery', 'Humidity'],
    'Average': [g, j, m, p],
    'Minimum': [h, k, n, q],
    'Maximum': [i, l, o, r]
}

w = pd.DataFrame(v)
w.to_csv('sensor_analysis_results.csv', index=False)
print("Results saved to 'sensor_analysis_results.csv'")

# Additional summary
x = {
    'Analysis_Type': ['Highest_Temperature_Time', 'Battery_Below_30_Count'],
    'Value': [t, u]
}

y = pd.DataFrame(x)
y.to_csv('sensor_summary.csv', index=False)
print("Summary saved to 'sensor_summary.csv'")

print("\nAnalysis complete!")
