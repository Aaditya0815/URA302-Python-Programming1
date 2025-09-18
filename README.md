# URA302 Python Programming - Mini Project: NumPy Basics

This repository contains two mini projects for the URA302 Python Programming course.

## Projects

### Project 1: Sensor Data Analysis
**File:** `project1_sensor_analysis.py`

Analyzes sensor readings collected by robots including:
- Temperature, distance, battery, and humidity sensors
- Calculates average, minimum, and maximum values for each sensor
- Finds the time when temperature was highest
- Counts number of times battery dropped below 30%
- Saves processed results to output files

### Project 2: Robot Path Analysis
**File:** `project2_robot_path_analysis.py`

Analyzes robot movement in a 2D grid world:
- Calculates total distance traveled by the robot
- Finds the farthest point from origin (0,0)
- Checks if robot ever revisited the same position
- Analyzes direction changes in the path
- Saves results to output files

## Data Files Required

- `sensor_data.csv` - Contains sensor readings with columns: timestamp, temperature, distance, battery, humidity
- `robot_path.csv` - Contains robot positions with columns: x, y coordinates

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run each project separately:

```bash
python project1_sensor_analysis.py
python project2_robot_path_analysis.py
```

## Output Files

Each project generates CSV files with analysis results:
- `sensor_analysis_results.csv` - Sensor statistics
- `sensor_summary.csv` - Key findings from sensor data
- `robot_path_results.csv` - Path analysis results
- `robot_path_summary.csv` - Detailed path data with distances

## Course Information

- **Course:** URA302 - Python Programming
- **Instructor:** Dr. Rohit Kumar Singla
- **Department:** Mechanical Engineering
