import pandas as pd

def load_data():
    logs = pd.read_csv("sample_data/data_access_logs.csv", parse_dates=["timestamp"])
    profiles = pd.read_csv("sample_data/user_profiles.csv")
    data = logs.merge(profiles, on="user_id", how="left", suffixes=('_log', '_prof'))
    data["hour"] = data["timestamp"].dt.hour
    data["rowcount"] = data.groupby("user_id")["user_id"].transform("count")
    return data