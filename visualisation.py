import matplotlib.pyplot as plt

def plot_risk_dashboard(df):
    # CRITICAL FIX: Check if rowcount exists. If not, recreate it immediately.
    if 'rowcount' not in df.columns:
        print("DEBUG: rowcount missing, recalculating...")
        df['rowcount'] = df.groupby("user_id")["user_id"].transform("count")
        
    plt.figure(figsize=(10, 6))
    
    # Use the now-guaranteed column
    scatter = plt.scatter(df['rowcount'], df['risk_score'], c=df['risk_score'], cmap='coolwarm', alpha=0.7)
    
    plt.colorbar(scatter, label='Risk Score')
    plt.title('Insider Threat Risk Dashboard: Volume vs. Severity')
    plt.xlabel('Access Volume (Frequency)')
    plt.ylabel('Risk Score')
    
    threshold = df["risk_score"].quantile(0.95)
    plt.axhline(y=threshold, color='r', linestyle='--', label=f'95th Percentile ({threshold:.1f})')
    
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig('risk_dashboard.png')
    plt.close() # Important: close to prevent Gradio memory leaks