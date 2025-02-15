from staging import temp_storage, data_validation
from processing import transformation, aggregation

def run_etl():
    # Load raw data from temporary storage
    raw_data = temp_storage.load_from_temp_storage()
    
    if not data_validation.validate_data(raw_data):
        print("Data validation failed.")
        return None

    transformed_data = transformation.transform(raw_data)
    
    aggregated_result = aggregation.aggregate([transformed_data])
    
    return aggregated_result

if __name__ == '__main__':
    result = run_etl()
    if result:
        print("ETL Pipeline Result:", result)
