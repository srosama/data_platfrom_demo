def validate_data(record):
    # Simple validation: check if required fields exist and types are correct
    try:
        record_id = int(record.get("id"))
        record_value = float(record.get("value"))
        return True
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    test_record = {"id": "10", "value": "200.5"}
    is_valid = validate_data(test_record)
    print(f"Record valid? {is_valid}")
