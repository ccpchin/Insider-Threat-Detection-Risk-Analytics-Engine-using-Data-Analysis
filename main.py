from data_loader import load_data
from feature_engineering import create_features
from baseline import build_baseline
from anomaly_detector import detect_anomalies
from risk_engine import compute_risk,assign_risk_label
from explain import add_explanations
import datetime

def main():
    try:
        df = load_data()
        df = create_features(df)
        baseline = build_baseline(df)
        df = detect_anomalies(df, baseline)
        df = compute_risk(df)
        df = add_explanations(df)
        if 'rowcount' not in df.columns:
            df['rowcount'] = df.groupby("user_id")["user_id"].transform("count")
        df.head(10).to_html("incident_report.html")
        with open("execution_log.txt", "a") as f:
            f.write(f"Run at {datetime.datetime.now()} | Max Risk: {df['risk_score'].max():.2f}\n")
        df["severity_label"] = df["risk_score"].apply(assign_risk_label)
        alerts = df.sort_values("risk_score", ascending=False).head(15)
        alerts.to_csv("security_audit_logs.csv", index=False)
        return df
        
    except Exception as e:
        print(f"Pipeline Error: {e}")
        return None