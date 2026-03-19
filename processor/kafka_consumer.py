from kafka import KafkaConsumer
import json
import psycopg2
from datetime import datetime
from prometheus_client import start_http_server, Counter, Histogram, Gauge

print("Starting consumer script...")

# Prometheus metrics
messages_processed = Counter(
    "iot_messages_processed_total",
    "Total number of IoT messages processed"
)

processing_time = Histogram(
    "iot_processing_seconds",
    "Time spent processing IoT messages"
)

kafka_lag = Gauge(
    "iot_kafka_lag",
    "Number of Kafka messages waiting to be processed"
)

# Start Prometheus metrics server
start_http_server(8000)

# Connect to Kafka
consumer = KafkaConsumer(
    "iot_stream",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="iot-consumer-group"
)

print("Connected to Kafka")

# Connect to PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    database="iot_db",
    user="admin",
    password="admin"
)

cursor = connection.cursor()

print("Connected to PostgreSQL")
print("Consumer waiting for messages...")

for message in consumer:

    with processing_time.time():

        data = message.value

        print("Received:", data)

        temperature = data["temperature"]

        status = "ALERT" if temperature > 80 else "NORMAL"

        cursor.execute(
            """
            INSERT INTO iot_analytics
            (device_id, temperature, humidity, status, event_time)
            VALUES (%s,%s,%s,%s,%s)
            """,
            (
                data["device_id"],
                data["temperature"],
                data["humidity"],
                status,
                data["event_time"]
            )
        )

        connection.commit()

        messages_processed.inc()

        # Estimate consumer lag
        partitions = consumer.assignment()
        for p in partitions:
            end_offset = consumer.end_offsets([p])[p]
            current_offset = consumer.position(p)
            lag = end_offset - current_offset
            kafka_lag.set(lag)

        print("Inserted into database")