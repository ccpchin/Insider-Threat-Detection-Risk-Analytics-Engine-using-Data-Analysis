from config import SENSITIVITY_MAP, DESTINATION_RISK

def create_features(df):
    df["sensitivity_score"] = df["resource_sensitivity"].map(SENSITIVITY_MAP).fillna(1)
    df["destination_score"] = df["action"].apply(lambda x: 4 if "EXPORT" in str(x).upper() else 1)
    df["is_off_hours"] = ((df["hour"] < 8) | (df["hour"] > 18)).astype(int)
    return df