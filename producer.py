# from __future__ import absolute_import
from kafka import KafkaProducer
import json
from useful_script import get_token_data
import time

# Json serialiser
def json_serialiser(data):
    return json.dumps(data).encode('utf-8')

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=json_serialiser
)

running = True

# Run Kafka producer
if __name__ == '__main__':
    try:
        while running:
            message = get_token_data()
            producer.send('ERC20-real-time-token', message) # Select topic for producer to send data over
            producer.flush()
            time.sleep(5) # Producer send data rate control
    except KeyboardInterrupt:
        running = False
    
producer.close()