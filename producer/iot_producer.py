from kafka import KafkaProducer
from faker import Faker
import json
import random
import time
from datetime import datetime

fake = Faker()

print("Producer starting...")

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TOPIC = "iot_stream"


def generate_sensor_data():

    data = {
        "device_id": fake.uuid4(),
        "temperature": round(random.uniform(20, 100), 2),
        "humidity": round(random.uniform(30, 90), 2),
        "event_time": datetime.utcnow().isoformat()
    }

    return data


while True:

    sensor_data = generate_sensor_data()

    producer.send(TOPIC, sensor_data)

    print("Sent:", sensor_data)

    time.sleep(0.1)