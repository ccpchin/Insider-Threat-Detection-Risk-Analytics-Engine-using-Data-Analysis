def generate_reasons(row):
    reasons = []
    time_limit = 3.0 if row.get("privilege_level") == "admin" else 2.0
    if row["time_score"] > time_limit:
        reasons.append(f"Unusual access at {row['hour']}:00")
    if row["volume_score"] > 2:
        reasons.append(f"Bulk data access: {row['rowcount']} records")
    if "EXPORT" in str(row["action"]).upper():
        reasons.append("High-risk export detected")
    if row["resource_sensitivity"] == "restricted" and row.get("privilege_level") == "user":
        reasons.append("Unauthorized access to restricted asset by standard user")
    return " | ".join(reasons)
def generate_narrative(row):
    narratives = []
    if row["risk_score"] > 70:
        narratives.append("CRITICAL: High-risk behavioral combination detected.")
    if "Unusual access time" in row["reasons"]:
        narratives.append(f"Activity occurred at {row['hour']}:00 outside standard hours.")
    if row["resource_sensitivity"] == "restricted":
        narratives.append(f"Access to restricted asset '{row['resource']}' flagged.")    
    return " | ".join(narratives) if narratives else "Normal user activity."
def add_explanations(df):
    df["reasons"] = df.apply(generate_reasons, axis=1)
    df["summary"] = df.apply(generate_narrative, axis=1)
    return df