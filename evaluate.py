
def evaluate(df):
    threshold = df["risk_score"].quantile(0.95)
    df["predicted"] = (df["risk_score"] > threshold).astype(int)
    print(f"\n--- Unsupervised Insight Report ---")
    print(f"Risk Threshold (95th Percentile): {threshold:.2f}")
    print(f"Total Events Flagged as High Risk: {df['predicted'].sum()}")
    print("This threshold adapts automatically to the data volume.")