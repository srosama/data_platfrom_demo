import os
import json
import yaml

def load_config():
    with open('config/staging.yaml', 'r') as f:
        return yaml.safe_load(f)

def save_to_temp_storage(data, filename="temp_data.json"):
    config = load_config()['staging']
    path = config['temp_storage_path']
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, filename)
    with open(full_path, 'w') as f:
        json.dump(data, f)
    print(f"Data saved to temporary storage at {full_path}")
    return full_path

def load_from_temp_storage(filename="temp_data.json"):
    config = load_config()['staging']
    full_path = os.path.join(config['temp_storage_path'], filename)
    with open(full_path, 'r') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    sample_data = {"id": 1, "value": 123.45}
    save_to_temp_storage(sample_data)
    data = load_from_temp_storage()
    print("Loaded data:", data)
