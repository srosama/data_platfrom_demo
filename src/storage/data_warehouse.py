import psycopg2
import yaml

def load_config():
    with open('config/storage.yaml', 'r') as f:
        return yaml.safe_load(f)

def insert_into_warehouse(record):
    config = load_config()['data_warehouse']
    conn = psycopg2.connect(
        host=config['host'],
        port=config['port'],
        database=config['database'],
        user=config['user'],
        password=config['password']
    )
    cur = conn.cursor()
    insert_query = """
        INSERT INTO processed_data (id, value)
        VALUES (%s, %s)
    """
    cur.execute(insert_query, (record['id'], record['value']))
    conn.commit()
    cur.close()
    conn.close()
    print("Record inserted into data warehouse.")

if __name__ == '__main__':
    sample_record = {"id": 1, "value": 150.0}
    insert_into_warehouse(sample_record)
