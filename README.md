# 🚀 Real-Time IoT Data Pipeline

## 📌 Overview

This project implements a **real-time data pipeline** that simulates IoT sensor data, processes it using a streaming architecture, and visualizes analytics and system performance through live dashboards.

The system is designed to handle **high-throughput streaming data with low latency**, while ensuring observability through monitoring tools.

---

## 🧠 Architecture

```
IoT Producer (Python)
        ↓
   Apache Kafka (Streaming)
        ↓
   Kafka Consumer (Processing)
        ↓
   PostgreSQL (Storage)
        ↓
   Streamlit Dashboard (Analytics)

Monitoring Layer:
Prometheus → Grafana
```

---

## ⚙️ Tech Stack

* **Streaming:** Apache Kafka
* **Processing:** Python (Kafka Consumer)
* **Database:** PostgreSQL
* **Monitoring:** Prometheus, Grafana
* **Visualization:** Streamlit
* **Containerization:** Docker

---

## 🔄 Data Flow

1. A Python-based **IoT producer** generates synthetic sensor data (temperature, humidity, device ID).
2. Data is streamed into a Kafka topic (`iot_stream`).
3. A **Kafka consumer** reads messages in real time and:

   * Processes the data
   * Classifies alerts (NORMAL / ALERT / CRITICAL)
   * Writes results into PostgreSQL
4. A **dashboard** displays:

   * Temperature trends
   * Alert distribution
   * Latest sensor readings
5. **Prometheus** collects system metrics
6. **Grafana** visualizes:

   * Throughput (events/sec)
   * Processing latency
   * Kafka consumer lag

---

## 📊 Features

* ✅ Real-time data streaming pipeline
* ✅ Parallel Kafka consumers (scalable processing)
* ✅ Alert classification system
* ✅ Live analytics dashboard
* ✅ Monitoring with Prometheus & Grafana
* ✅ Kafka consumer lag tracking
* ✅ Sub-second processing latency

---

## 📈 Monitoring Metrics

The system tracks key performance indicators:

* `iot_messages_processed_total` → Total events processed
* `events/sec` → Pipeline throughput
* `iot_processing_seconds` → Processing latency
* `iot_kafka_lag` → Consumer backlog

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-url>
cd real_time_iot_pipeline
```

---

### 2. Start Infrastructure

```
docker compose up -d
```

This starts:

* Kafka
* Zookeeper
* PostgreSQL
* Prometheus
* Grafana

---

### 3. Run the Producer

```
python producer/iot_producer.py
```

---

### 4. Run the Consumer

```
python processor/kafka_consumer.py
```

(Optional: run multiple consumers for parallel processing)

---

### 5. Run the Dashboard

```
streamlit run dashboard/app.py
```

---

### 6. Access Services

| Tool       | URL                   |
| ---------- | --------------------- |
| Dashboard  | http://localhost:8501 |
| Prometheus | http://localhost:9090 |
| Grafana    | http://localhost:3000 |

---

## 📊 Grafana Dashboard

The monitoring dashboard includes:

* 📈 IoT Messages Processed
* ⚡ Events Per Second
* ⏱️ Average Processing Time
* 📉 Kafka Consumer Lag

---

## 🧪 Example Data

```
{
  "device_id": "b210a19c-65e5-4c31-ade8",
  "temperature": 85.2,
  "humidity": 60.4,
  "event_time": "2026-03-15T03:26:14"
}
```

---

## 🎯 Key Achievements

* Designed a **scalable streaming architecture**
* Achieved **near real-time processing (< 5ms latency)**
* Built a **fully observable pipeline** with monitoring
* Implemented **end-to-end data flow from ingestion to visualization**

---

## 📌 Future Improvements

* Add schema validation (Avro + Schema Registry)
* Deploy to cloud (AWS / GCP)
* Add anomaly detection (ML model)
* Implement data partitioning strategies

---

## 👤 Author

**Muneeb Ahmed**
LinkedIn: https://www.linkedin.com/in/muneebahmed18/ 
MS Data Science Student

---

## ⭐ Why This Project Matters

This project demonstrates:

* Real-world data engineering concepts
* Streaming architecture design
* Monitoring and observability best practices

It reflects the type of systems used in modern data platforms handling **high-volume real-time data**.

---
