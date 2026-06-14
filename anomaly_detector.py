import numpy as np

def detect_anomalies(df, baseline):
    df = df.merge(baseline, on="user_id", how="left")
    df["hour_mean"] = df["hour_mean"].fillna(df["hour"].mean())
    df["hour_std"] = df["hour_std"].fillna(1)
    df["rowcount_mean"] = df["rowcount_mean"].fillna(df["rowcount"].mean())
    df["rowcount_std"] = df["rowcount_std"].fillna(1)
    df["time_score"] = abs(df["hour"] - df["hour_mean"]) / (df["hour_std"] + 1)
    df["volume_score"] = (df["rowcount"] - df["rowcount_mean"]) / (df["rowcount_std"] + 1)
    df["volume_score"] = df["volume_score"].clip(lower=0)
    return df