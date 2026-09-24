# edge-ai-telemetry-service
Edge AI Telemetry Service for Anomaly Detection in Sensor Streams
# ⚡ Edge AI Micro-Telemetry Service

A lightweight **Edge AI Telemetry Service** designed for real-time monitoring and anomaly detection in hardware sensor streams (temperature, vibration, pressure).

---

## 🚀 KEY FEATURES

- **Edge Anomaly Detection:** Uses Z-score statistical evaluation to identify hardware spikes with zero latency.
- **Resource Efficient:** Runs directly on low-power embedded microcontrollers and edge gateways.
- **Telemetry Stream Analytics:** Flags critical sensor faults before system-level failure occurs.

---

## 🛠️ TECH STACK

- **Language:** Python 3
- **Core Domain:** ECE (Telemetry & Sensor Analytics) + Edge AI
- **Libraries:** Pure Python / NumPy

---

## 💻 SAMPLE OUTPUT

```text
--- Edge AI Micro-Telemetry Monitor Active ---
[NORMAL_TELEMETRY] TEMP_SENS_01 -> Value: 30.2 | Z-Score: 0.13
[NORMAL_TELEMETRY] TEMP_SENS_01 -> Value: 29.8 | Z-Score: 0.13
[NORMAL_TELEMETRY] TEMP_SENS_01 -> Value: 31.1 | Z-Score: 0.73
[CRITICAL_ANOMALY] TEMP_SENS_01 -> Value: 39.5 | Z-Score: 6.33
[NORMAL_TELEMETRY] TEMP_SENS_01 -> Value: 30.0 | Z-Score: 0.0
```

---

## ⚙️ HOW TO RUN LOCALLY

1. Clone the repository:
   ```bash
   git clone [https://github.com/akhila64b-sudo/edge-ai-telemetry-service.git](https://github.com/akhila64b-sudo/edge-ai-telemetry-service.git)
   ```
2. Run the analyzer script:
   ```bash
   python edge_telemetry.py
   ```
