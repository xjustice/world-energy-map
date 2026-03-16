
import csv
import json
import urllib.request

OWID_URL = 'https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv'
OUTPUT_FILE = 'data.json'

def build_data():
    print(f"Downloading data from {OWID_URL}...")
    response = urllib.request.urlopen(OWID_URL)
    lines = [line.decode('utf-8') for line in response.readlines()]
    reader = csv.DictReader(lines)
    
    electricity_data = {}
    
    for row in reader:
        iso = row.get('iso_code')
        year = row.get('year')
        value = row.get('per_capita_electricity')
        
        if iso and value and value.strip():
            try:
                val_float = float(value)
                year_int = int(year)
                
                if iso not in electricity_data or year_int > electricity_data[iso]['year']:
                    electricity_data[iso] = {
                        'value': val_float,
                        'year': year_int
                    }
            except ValueError:
                continue
                
    print(f"Processed {len(electricity_data)} countries. Saving to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(electricity_data, f, indent=2)
    print("Success!")

if __name__ == "__main__":
    build_data()
