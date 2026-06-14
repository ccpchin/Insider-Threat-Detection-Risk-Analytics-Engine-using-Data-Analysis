Architecture
The system follows a modular pipeline architecture designed for high maintainability:
1) Ingestion (data_loader.py): Normalizes disparate logs into a unified DataFrame.
2) Feature Engineering (feature_engineering.py): Converts raw categorical data into numerical risk indicators using weighted mapping.
3) Baseline Modeling (baseline.py): Calculates Z-score based behavioral baselines per user.
4) Detection & Risk Engine (anomaly_detector.py, risk_engine.py): Employs statistical outlier detection (IQR/Z-Score) combined with role-based escalation (e.g., Interns vs. Admins) to calculate a 0-100 risk score.
5) Investigation UI (app.py, visualisation.py): Provides an interactive Gradio dashboard and visual scatter-plot analytics.

Analysis Algorithms
1) We utilize Statistical Profiling over black-box ML to ensure 100% explainability for auditors.
2) Anomaly Detection: Uses standardized scores based on mean/std deviations from the user’s 365-day baseline.
3) Scalability: The architecture is designed to be infrastructure-agnostic. While currently batch-processing CSVs, the modular design allows for immediate migration to Apache Spark for distributed compute or Kafka for real-time streaming, capable of handling 1M+ daily events.

UI Design
1) Gradio-based: Chosen for rapid, browser-based interactivity.
2) Prioritization: The UI surfaces a "Prioritized Investigation Queue" rather than raw logs, reducing alert fatigue by focusing on high-risk labels (CRITICAL/HIGH/MEDIUM) first.
