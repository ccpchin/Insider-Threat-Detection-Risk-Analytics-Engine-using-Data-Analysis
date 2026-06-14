import gradio as gr
from main import main
from visualisation import plot_risk_dashboard

# app.py
def get_dashboard_data():
    df = main()
    if df is None or df.empty: return None, None
    plot_risk_dashboard(df)
    display_cols = ["username", "severity_label", "risk_score", "reasons", "department", "job_title"]
    return df[display_cols], "risk_dashboard.png"

with gr.Blocks(title="Security Intel Dashboard") as demo:
    gr.Markdown("Insider Threat Detection System using Data Analysis")
    with gr.Row():
        btn = gr.Button("Analyze System Logs")
    with gr.Row():
        table = gr.DataFrame(label="Prioritized Investigation Queue")
        plot = gr.Image(label="Risk Distribution Plot")
    btn.click(get_dashboard_data, outputs=[table, plot])
if __name__ == "__main__":
    demo.launch()