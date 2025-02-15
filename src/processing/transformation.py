import yaml

def load_config():
    with open('config/processing.yaml', 'r') as f:
        return yaml.safe_load(f)

def transform(record):
    config = load_config()['processing']['transformation']
    scale_factor = config.get('scale_factor', 1)
    # For example, scale the 'value'
    record['value'] = record.get('value', 0) * scale_factor
    return record

if __name__ == '__main__':
    sample = {"id": 1, "value": 100}
    transformed = transform(sample)
    print("Transformed record:", transformed)
