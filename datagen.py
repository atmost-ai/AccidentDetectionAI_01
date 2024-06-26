import csv
import uuid
from datetime import datetime, timedelta
import random
import os

KOCHI_COORDINATES = {"latitude": 9.939093, "longitude": 76.270523}
TRV_COORDINATES = {"latitude": 8.5241, "longitude": 76.9366}
LATITUDE_INCREMENT = (TRV_COORDINATES['latitude'] - KOCHI_COORDINATES['latitude']) / 100
LONGITUDE_INCREMENT = (TRV_COORDINATES['longitude'] - KOCHI_COORDINATES['longitude']) / 100

start_time = datetime.now()
start_location = KOCHI_COORDINATES.copy()

vehicle_ids = [f'KL-07-{i}' for i in range(1000)]
make_and_model = [
    "Maruti-Suzuki Alto", "Maruti-Suzuki Wagon R", "Maruti-Suzuki Swift", "Maruti-Suzuki Dzire", "Maruti-Suzuki Baleno",
    "Maruti-Suzuki Vitara Brezza", "Maruti-Suzuki Ertiga", "Maruti-Suzuki Celerio", "Maruti-Suzuki S-Presso", "Maruti-Suzuki Ignis",
    "Maruti-Suzuki Ciaz", "Maruti-Suzuki XL6", "Hyundai Santro", "Hyundai Grand i10 Nios", "Hyundai i20",
    "Hyundai Venue", "Hyundai Creta", "Hyundai Verna", "Hyundai Elantra", "Hyundai Tucson",
    "Tata Tiago", "Tata Tigor", "Tata Altroz", "Tata Nexon", "Tata Harrier",
    "Tata Safari", "Mahindra Thar", "Mahindra XUV300", "Mahindra XUV500", "Mahindra XUV700",
    "Mahindra Scorpio", "Mahindra Bolero", "Mahindra Marazzo", "Mahindra Alturas G4", "Kia Seltos",
    "Kia Sonet", "Kia Carnival", "Toyota Glanza", "Toyota Urban Cruiser", "Toyota Yaris",
    "Toyota Innova Crysta", "Toyota Fortuner", "Honda Amaze", "Honda Jazz", "Honda WR-V",
    "Honda City", "Honda Civic", "Honda CR-V", "Ford Figo", "Ford Aspire",
    "Ford Freestyle", "Ford EcoSport", "Ford Endeavour", "Renault Kwid", "Renault Triber",
    "Renault Kiger", "Renault Duster", "Nissan Magnite", "Nissan Kicks", "Volkswagen Polo",
    "Volkswagen Vento", "Volkswagen Taigun", "Skoda Rapid", "Skoda Octavia", "Skoda Superb",
    "Skoda Kushaq", "Skoda Kodiaq", "MG Hector", "MG Hector Plus", "MG ZS EV",
    "MG Gloster", "Jeep Compass", "Jeep Wrangler", "Fiat Urban Cross", "Fiat Linea",
    "Fiat Punto Evo", "Datsun redi-GO", "Datsun GO", "Datsun GO+", "Mercedes-Benz A-Class",
    "Mercedes-Benz GLA", "Mercedes-Benz C-Class", "Mercedes-Benz E-Class", "BMW 3 Series", "BMW 5 Series",
    "BMW X1", "BMW X3", "Audi A3", "Audi A4", "Audi Q3",
    "Audi Q5", "Audi Q7", "Jaguar XE", "Jaguar XF", "Jaguar F-Pace",
    "Land Rover Range Rover Evoque", "Land Rover Discovery Sport", "Volvo XC40", "Volvo XC60", "Porsche Macan"
]


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

def determine_severity():
    severity_chance = random.random()
    if severity_chance < 0.5:
        return "Low"
    elif severity_chance < 0.8:
        return "Medium"
    else:
        return "High"

def generate_vehicle_data(vehicle_id):
    location = simulate_vehicle_movement()
    return {
        'id': uuid.uuid4(),
        'vehicle_id': vehicle_id,
        'timestamp': get_next_time().isoformat(),
        'location': (location['latitude'], location['longitude']),
        'speed': random.uniform(10, 90),
        'direction': 'North-East',
        'make_and_model': random.choice(make_and_model),
        'year': random.choice(['2015', '2016', '2017', '2018', '2019', '2020', '2021']),
        'fuelType': random.choice(["Petrol", "Diesel", "Electric", "Hybrid"]),
        'severity': "None"
    }

def generate_accelerometer_data(vehicle_id, timestamp, is_accident=False):
    severity = None
    if is_accident:
        severity = determine_severity()
        x_value = random.uniform(15, 20) if severity == "High" else random.uniform(10, 15) if severity == "Medium" else random.uniform(5, 10)
        y_value = random.uniform(15, 20) if severity == "High" else random.uniform(10, 15) if severity == "Medium" else random.uniform(5, 10)
    else:
        x_value = random.uniform(-10, 10)
        y_value = random.uniform(-10, 10)
    return {
        'id': uuid.uuid4(),
        'vehicle_id': vehicle_id,
        'actual_time': timestamp,
        'time_interval': random.uniform(0, 1),
        'X': x_value,
        'Y': y_value,
        'timestamp': timestamp,
        'severity': severity
    }

def generate_gyroscope_data(vehicle_id, timestamp, is_accident=False):
    severity = None
    if is_accident:
        severity = determine_severity()
        angular_velocity = random.uniform(180, 360) if severity == "High" else random.uniform(90, 180) if severity == "Medium" else random.uniform(45, 90)
    else:
        angular_velocity = random.uniform(-180, 180)
    return {
        'id': uuid.uuid4(),
        'vehicle_id': vehicle_id,
        'angular_velocity': angular_velocity,
        'timestamp': timestamp,
        'severity': severity
    }


def generate_gps_data(vehicle_id, timestamp, is_accident=False):
    location = simulate_vehicle_movement()
    severity = None
    if is_accident:
        severity = determine_severity()
        if severity == "High":
            latitude_deviation = random.uniform(-0.008, 0.008)
            longitude_deviation = random.uniform(-0.008, 0.008)
        elif severity == "Medium":
            latitude_deviation = random.uniform(-0.004, 0.004)
            longitude_deviation = random.uniform(-0.004, 0.004)
        else:  # Low severity
            latitude_deviation = random.uniform(-0.002, 0.002)
            longitude_deviation = random.uniform(-0.002, 0.002)
        
        location['latitude'] += latitude_deviation
        location['longitude'] += longitude_deviation

    return {
        'id': uuid.uuid4(),
        'vehicle_id': vehicle_id,
        'latitude': location['latitude'],
        'longitude': location['longitude'],
        'timestamp': timestamp,
        'severity': severity
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

    for _ in range(100):
        vehicle_id = random.choice(vehicle_ids)
        timestamp = get_next_time().isoformat()
        is_accident = random.random() < 0.01  # 1% chance of an accident for each record
        
        vehicle_data = generate_vehicle_data(vehicle_id)
        vehicle_data['severity'] = determine_severity() if is_accident else "None"
        vehicle_data_list.append(vehicle_data)

        accelerometer_data_list.append(generate_accelerometer_data(vehicle_id, timestamp, is_accident))
        gyroscope_data_list.append(generate_gyroscope_data(vehicle_id, timestamp, is_accident))
        gps_data_list.append(generate_gps_data(vehicle_id, timestamp, is_accident))

    vehicle_fieldnames = ['id', 'vehicle_id', 'timestamp', 'location', 'speed', 'direction', 'make_and_model', 'year', 'fuelType', 'severity']
    accelerometer_fieldnames = ['id', 'vehicle_id', 'actual_time', 'time_interval', 'X', 'Y', 'Z', 'timestamp', 'severity']
    gyroscope_fieldnames = ['id', 'vehicle_id', 'angular_velocity', 'timestamp', 'severity']
    gps_fieldnames = ['id', 'vehicle_id', 'latitude', 'longitude', 'timestamp', 'severity']

    write_csv('vehicle_data.csv', vehicle_fieldnames, vehicle_data_list)
    write_csv('accelerometer_data.csv', accelerometer_fieldnames, accelerometer_data_list)
    write_csv('gyroscope_data.csv', gyroscope_fieldnames, gyroscope_data_list)
    write_csv('gps_data.csv', gps_fieldnames, gps_data_list)
