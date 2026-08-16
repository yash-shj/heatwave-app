THRESHOLD_C = 40.0

def check_heatwave(region, temperature):
    """Return True if the given temperature triggers a heatwave alert."""
    return temperature >= THRESHOLD_C

def classify_regions(readings):
    """readings: dict of {region: temperature}
    Returns dict of {region: 'ALERT' or 'NORMAL'}"""
    return {
        region: 'ALERT' if check_heatwave(region, temp) else 'NORMAL'
        for region, temp in readings.items()
    }

if __name__ == '__main__':
    sample_readings = {
        'Mumbai': 38.5,
        'Nagpur': 42.0,
        'Pune': 36.0,
        'Nashik': 41.2,
    }
    results = classify_regions(sample_readings)
    for region, status in results.items():
        print(f'{region}: {status}')
