def aggregate(records):
    # A simple aggregation: sum all 'value' fields
    total = sum(record.get('value', 0) for record in records)
    return {"total_value": total}

if __name__ == '__main__':
    sample_records = [
        {"id": 1, "value": 100},
        {"id": 2, "value": 150},
        {"id": 3, "value": 200}
    ]
    aggregated = aggregate(sample_records)
    print("Aggregated result:", aggregated)
