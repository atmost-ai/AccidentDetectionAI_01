# Accident Detection Data Simulation

This project simulates vehicle, accelerometer, gyroscope, and GPS data to detect accident events and categorize their severity. The generated data is saved into CSV files, which can be used for further analysis and model training.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Generation](#data-generation)
  - [Vehicle Data](#vehicle-data)
  - [Accelerometer Data](#accelerometer-data)
  - [Gyroscope Data](#gyroscope-data)
  - [GPS Data](#gps-data)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [License](#license)

## Project Overview

The purpose of this project is to generate synthetic data representing the movement of vehicles along with accelerometer, gyroscope, and GPS data. Accident events are simulated randomly, and the severity of these accidents is categorized as "Low", "Medium", or "High".

## Data Generation

### Vehicle Data
- **Fields:** `id`, `vehicle_id`, `timestamp`, `location`, `speed`, `direction`, `make`, `model`, `year`, `fuelType`, `severity`
- **Description:** Contains information about the vehicle's movement and properties.

### Accelerometer Data
- **Fields:** `id`, `vehicle_id`, `actual_time`, `time_interval`, `X`, `Y`, `timestamp`, `severity`
- **Description:** Contains data from the vehicle's accelerometer sensor.

### Gyroscope Data
- **Fields:** `id`, `vehicle_id`, `angular_velocity`, `timestamp`, `severity`
- **Description:** Contains data from the vehicle's gyroscope sensor.

### GPS Data
- **Fields:** `id`, `vehicle_id`, `latitude`, `longitude`, `timestamp`, `severity`
- **Description:** Contains data from the vehicle's GPS sensor.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/accident-detection-simulation.git
    cd accident-detection-simulation
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```


## Usage

To generate the data, simply run the `data_generation.py` script:
```bash
python datagen.py
