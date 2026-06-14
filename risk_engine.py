from config import WEIGHTS, RISK_THRESHOLDS

from config import WEIGHTS

def compute_risk(df):
    # Base risk score
    df["risk_score"] = (WEIGHTS["time"] * df["time_score"] + WEIGHTS["volume"] * df["volume_score"] + WEIGHTS["sensitivity"] * df["sensitivity_score"] + WEIGHTS["destination"] * df["destination_score"] + WEIGHTS["behavior"] * df["is_off_hours"]) * 20
    mask_intern_restricted = (df["privilege_level"].isin(["user", "intern"])) & (df["resource_sensitivity"] == "restricted")
    df.loc[mask_intern_restricted, "risk_score"] += 30
    mask_admin_offhours = (df["privilege_level"] == "admin") & (df["is_off_hours"] == 1)
    df.loc[mask_admin_offhours, "risk_score"] += 20
    return df

def assign_risk_label(score):
    if score >= RISK_THRESHOLDS["critical"]:
        return "CRITICAL"
    elif score >= RISK_THRESHOLDS["high"]:
        return "HIGH"
    elif score >= RISK_THRESHOLDS["medium"]:
        return "MEDIUM"
    else:
        return "LOW"