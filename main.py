import csv
import uuid
from datetime import datetime, timedelta
import random
import os

LONDON_COORDINATES = {"latitude": 9.939093, "longitude": 76.270523}
BIRMINGHAM_COORDINATES = {"latitude": 52.4862, "longitude": -1.8904}
LATITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['latitude'] - LONDON_COORDINATES['latitude']) / 100
LONGITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['longitude'] - LONDON_COORDINATES['longitude']) / 100

start_time = datetime.now()
start_location = LONDON_COORDINATES.copy()

vehicle_ids = [f'KL-07-{i}' for i in range(1000)]

def get_next_time():
    global start_time
    start_time += timedelta(seconds=random.randint(30, 60))
    return start_time

def simulate_vehicle_movement():
    global start_location
    start_location['latitude'] += LATITUDE_INCREMENT
    start_location['longitude'] += LONGITUDE_INCREMENT
    start_location['latitude'] += random.uniform(-0.0005, 0.0005)
    start_location['longitude'] += random.uniform(-0.0005, 0.0005)
    return start_location

def generate_vehicle_data(vehicle_id):
    location = simulate_vehicle_movement()
    return {
        'id': uuid.uuid4(),
        'vehicle_id': vehicle_id,
        'timestamp': get_next_time().isoformat(),
        'location': (location['latitude'], location['longitude']),
        'speed': random.uniform(10, 40),
        'direction': 'North-East',
        'make': 'Tesla',
        'model': 'Model S',
        'year': 2024,
        'fuelType': 'Electric'
    }

def generate_accelerometer_data(vehicle_id, timestamp):
    return {
        'id': uuid.uuid4(),
        'vehicle_id': vehicle_id,
        'actual_time': timestamp,
        'time_interval': random.uniform(0, 1),
        'X': random.uniform(-10, 10),
        'Y': random.uniform(-10, 10),
        'timestamp': timestamp
    }

def generate_gyroscope_data(vehicle_id, timestamp):
    return {
        'id': uuid.uuid4(),
        'vehicle_id': vehicle_id,
        'angular_velocity': random.uniform(-180, 180),
        'timestamp': timestamp
    }

def generate_gps_data(vehicle_id, timestamp):
    location = simulate_vehicle_movement()
    return {
        'id': uuid.uuid4(),
        'vehicle_id': vehicle_id,
        'latitude': location['latitude'],
        'longitude': location['longitude'],
        'timestamp': timestamp
    }

def write_csv(file_name, fieldnames, data):
    # Ensure the 'data' directory exists
    os.makedirs('data', exist_ok=True)
    
    # Create the full path for the CSV file
    full_path = os.path.join('data', file_name)
    
    # Write the data to the CSV file
    with open(full_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    vehicle_data_list = []
    accelerometer_data_list = []
    gyroscope_data_list = []
    gps_data_list = []

    for _ in range(10000):
        vehicle_id = random.choice(vehicle_ids)
        timestamp = get_next_time().isoformat()
        
        vehicle_data_list.append(generate_vehicle_data(vehicle_id))
        accelerometer_data_list.append(generate_accelerometer_data(vehicle_id, timestamp))
        gyroscope_data_list.append(generate_gyroscope_data(vehicle_id, timestamp))
        gps_data_list.append(generate_gps_data(vehicle_id, timestamp))

    vehicle_fieldnames = ['id', 'vehicle_id', 'timestamp', 'location', 'speed', 'direction', 'make', 'model', 'year', 'fuelType']
    accelerometer_fieldnames = ['id', 'vehicle_id', 'actual_time', 'time_interval', 'X', 'Y', 'timestamp']
    gyroscope_fieldnames = ['id', 'vehicle_id', 'angular_velocity', 'timestamp']
    gps_fieldnames = ['id', 'vehicle_id', 'latitude', 'longitude', 'timestamp']

    write_csv('vehicle_data.csv', vehicle_fieldnames, vehicle_data_list)
    write_csv('accelerometer_data.csv', accelerometer_fieldnames, accelerometer_data_list)
    write_csv('gyroscope_data.csv', gyroscope_fieldnames, gyroscope_data_list)
    write_csv('gps_data.csv', gps_fieldnames, gps_data_list)
