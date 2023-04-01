from kafka import KafkaConsumer
import json
from useful_script import write_token_data

def json_deserializer(data):
        return json.loads(data)

consumer = KafkaConsumer(
    'ERC20-real-time-token', # Select topic for consumer to get data from
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    value_deserializer=json_deserializer
)

for msg in consumer:
    write_token_data(msg.value)