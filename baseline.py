def build_baseline(df):
    baseline = df.groupby("user_id").agg({"hour": ["mean", "std"],"rowcount": ["mean", "std"]}) 
    baseline.columns = ["_".join(col) for col in baseline.columns]
    baseline = baseline.reset_index()
    return baseline