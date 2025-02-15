import json
from confluent_kafka import Consumer
import yaml

def load_config():
    with open('config/ingestion.yaml', 'r') as f:
        return yaml.safe_load(f)

def kafka_consume():
    config = load_config()['kafka']
    consumer_conf = {
        'bootstrap.servers': config['broker'],
        'group.id': 'data-platform-group',
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(consumer_conf)
    consumer.subscribe([config['topic']])
    
    try:
        msg = consumer.poll(1.0)
        if msg is None:
            return None
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            return None
        data = json.loads(msg.value().decode('utf-8'))
        return data
    finally:
        consumer.close()

if __name__ == '__main__':
    data = kafka_consume()
    if data:
        print("Consumed data:", data)
