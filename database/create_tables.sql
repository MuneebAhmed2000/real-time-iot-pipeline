CREATE TABLE iot_analytics (
    id SERIAL PRIMARY KEY,
    device_id TEXT,
    temperature FLOAT,
    humidity FLOAT,
    status TEXT,
    event_time TIMESTAMP,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);