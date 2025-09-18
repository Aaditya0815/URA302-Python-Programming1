# Project 2: Robot Path Analysis
# URA302 - Python Programming Mini Project

import numpy as np
import pandas as pd

# Load robot path data from CSV file
print("Loading robot path data...")
a = pd.read_csv('robot_path.csv')

# Convert to numpy arrays for calculations
b = a['x'].values
c = a['y'].values

print("Robot Path Analysis Results:")
print("=" * 35)

# Calculate total distance traveled by the robot
print("\n1. TOTAL DISTANCE TRAVELED:")
print("-" * 28)
d = 0  # Initialize total distance
e = len(b)  # Number of points

for i in range(1, e):
    f = b[i] - b[i-1]  # x difference
    g = c[i] - c[i-1]  # y difference
    h = np.sqrt(f*f + g*g)  # Distance between consecutive points
    d += h

print(f"Total distance traveled: {d:.2f} units")

# Find farthest point from origin (0,0)
print("\n2. FARTHEST POINT FROM ORIGIN:")
print("-" * 30)
i = 0  # Initialize maximum distance
j = 0  # Index of farthest point

for k in range(e):
    l = np.sqrt(b[k]*b[k] + c[k]*c[k])  # Distance from origin
    if l > i:
        i = l
        j = k

m = b[j]  # x coordinate of farthest point
n = c[j]  # y coordinate of farthest point
print(f"Farthest point: ({m}, {n})")
print(f"Distance from origin: {i:.2f} units")

# Check if robot ever revisited the same position
print("\n3. POSITION REVISIT CHECK:")
print("-" * 25)
o = False  # Flag for revisit
p = 0  # Number of revisits

# Create a list of (x,y) tuples for comparison
q = []
for r in range(e):
    s = (b[r], c[r])
    q.append(s)

# Check for duplicates
t = len(q)
u = len(set(q))  # Set removes duplicates

if t != u:
    o = True
    p = t - u  # Number of duplicate positions

if o:
    print(f"Robot revisited positions: YES")
    print(f"Number of position revisits: {p}")
else:
    print("Robot revisited positions: NO")

# Additional analysis - direction changes
print("\n4. PATH ANALYSIS:")
print("-" * 16)
v = 0  # Direction change count
w = 0  # Previous direction

for x in range(2, e):
    y = b[x] - b[x-1]  # Current x movement
    z = c[x] - c[x-1]  # Current y movement
    
    aa = b[x-1] - b[x-2]  # Previous x movement
    bb = c[x-1] - c[x-2]  # Previous y movement
    
    # Check if direction changed (simplified)
    if (y > 0 and aa < 0) or (y < 0 and aa > 0) or (z > 0 and bb < 0) or (z < 0 and bb > 0):
        v += 1

print(f"Number of direction changes: {v}")

# Save results to output file
print("\n5. SAVING RESULTS:")
print("-" * 18)
cc = {
    'Analysis': ['Total_Distance', 'Farthest_X', 'Farthest_Y', 'Max_Distance_From_Origin', 'Revisited_Positions', 'Direction_Changes'],
    'Value': [d, m, n, i, 'Yes' if o else 'No', v]
}

dd = pd.DataFrame(cc)
dd.to_csv('robot_path_results.csv', index=False)
print("Results saved to 'robot_path_results.csv'")

# Save path summary
ee = {
    'Point_Number': range(e),
    'X_Coordinate': b,
    'Y_Coordinate': c,
    'Distance_From_Origin': [np.sqrt(b[i]*b[i] + c[i]*c[i]) for i in range(e)]
}

ff = pd.DataFrame(ee)
ff.to_csv('robot_path_summary.csv', index=False)
print("Path summary saved to 'robot_path_summary.csv'")

print("\nAnalysis complete!")
