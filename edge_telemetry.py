"""
Edge AI Micro-Telemetry Service
Simulates streaming sensor telemetry (e.g., Temperature, Vibration) 
and performs lightweight Edge AI anomaly detection using Z-score statistics.
"""

import math
import time

class EdgeTelemetryAnalyzer:
    def __init__(self, baseline_mean=25.0, baseline_std=2.0, anomaly_threshold=3.0):
        self.mean = baseline_mean
        self.std = baseline_std
        self.threshold = anomaly_threshold

    def evaluate_sample(self, sensor_id: str, reading: float) -> dict:
        """Calculates Z-score on the edge to flag high-variance anomalies."""
        z_score = abs(reading - self.mean) / self.std
        is_anomaly = z_score > self.threshold
        
        status = "CRITICAL_ANOMALY" if is_anomaly else "NORMAL_TELEMETRY"
        
        return {
            "sensor_id": sensor_id,
            "value": reading,
            "z_score": round(z_score, 2),
            "status": status,
            "edge_processed": True
        }

if __name__ == "__main__":
    analyzer = EdgeTelemetryAnalyzer(baseline_mean=30.0, baseline_std=1.5)
    
    # Simulated live micro-telemetry stream
    telemetry_stream = [
        ("TEMP_SENS_01", 30.2),
        ("TEMP_SENS_01", 29.8),
        ("TEMP_SENS_01", 31.1),
        ("TEMP_SENS_01", 39.5),  # Thermal spike anomaly
        ("TEMP_SENS_01", 30.0)
    ]
    
    print("--- Edge AI Micro-Telemetry Monitor Active ---")
    for sensor, val in telemetry_stream:
        res = analyzer.evaluate_sample(sensor, val)
        print(f"[{res['status']}] {res['sensor_id']} -> Value: {res['value']} | Z-Score: {res['z_score']}")
        time.sleep(0.1)
