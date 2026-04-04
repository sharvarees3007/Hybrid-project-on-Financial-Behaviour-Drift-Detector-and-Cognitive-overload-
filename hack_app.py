from nicegui import ui
import pandas as pd
import numpy as np

# 1. ENHANCED DATA LOGIC (Hackathon Simulation)
def get_hybrid_data():
    # Simulated data with a 'correlation spike' for the demo
    sessions = np.arange(1, 21)
    # Simulate stress rising then falling
    stress = [3, 4, 3.5, 7.8, 8.2, 8.5, 4, 3.5, 3, 2.5, 6, 7.2, 3, 3, 4, 5, 8.1, 4, 3, 3]
    # Simulate drift tracking with stress
    drift = [20, 25, 22, 85, 92, 88, 30, 25, 20, 15, 60, 75, 20, 20, 25, 35, 88, 30, 20, 20]
    
    return pd.DataFrame({
        'Session': sessions,
        'Cognitive_Load': stress,
        'Financial_Drift': drift
    })

df = get_hybrid_data()

# 2. STYLING & UI SETUP
ui.query('body').style('background-color: #0E1117; color: #00FFC8; font-family: "Segoe UI", sans-serif;')

with ui.header().classes('items-center justify-between shadow-lg').style('background-color: #1A1C23; border-bottom: 2px solid #00FFC8'):
    ui.label('⚡ HYBRID BEHAVIORAL COMMAND CENTER').classes('text-2xl font-black italic')
    with ui.row().classes('items-center'):
        ui.badge('HACKATHON BUILD v2.0', color='orange')
        ui.button(icon='refresh', on_click=lambda: ui.notify('Re-calculating Hybrid Vectors...')).props('flat color=white')

# 3. DASHBOARD BODY
with ui.row().classes('w-full justify-center mt-6'):
    
    # LEFT: CONTROL PANEL
    with ui.card().classes('p-6 shadow-2xl').style('background-color: #1A1C23; border: 1px solid #333; width: 350px; border-radius: 15px'):
        ui.label('ALGORITHM WEIGHTS').classes('text-lg font-bold text-white mb-4')
        
        ui.label('Cognitive Sensitivity (W1)')
        w1 = ui.slider(min=0, max=1, step=0.1, value=0.4).props('label-always color=cyan selection-color=white')
        
        ui.label('Behavioral Drift (W2)')
        w2 = ui.slider(min=0, max=1, step=0.1, value=0.6).props('label-always color=pink selection-color=white')
        
        ui.separator().classes('my-4')
        
        # REAL-TIME RISK INDICATOR
        ui.label('HYBRID RISK ANALYSIS').classes('text-sm text-gray-400')
        risk_badge = ui.label('STABLE').classes('text-center w-full py-2 rounded-lg font-bold mt-2')
        risk_badge.style('background-color: #00FFC8; color: #0E1117')

    # RIGHT: ANALYTICS CHART
    with ui.card().classes('p-4').style('background-color: #1A1C23; border: 1px solid #333; width: 800px; border-radius: 15px'):
        # Using Matplotlib-style line plot for high-contrast dark mode
        plot = ui.line_plot(n=2, limit=20, update_every=1).with_legend(['Stress Index', 'Drift Magnitude'], loc='upper left')
        plot.style('width: 100%; height: 400px;')

# 4. LIVE UPDATE LOGIC
def update_dashboard():
    # Push data to plot
    plot.push(df['Session'].tolist(), [df['Cognitive_Load'].tolist(), df['Financial_Drift'].tolist()])
    
    # Calculate Risk Score: (Average Stress * W1) + (Average Drift/10 * W2)
    avg_stress = df['Cognitive_Load'].mean()
    avg_drift = df['Financial_Drift'].mean()
    risk_score = (avg_stress * w1.value) + (avg_drift/10 * w2.value)
    
    # Update Risk UI
    if risk_score > 6.5:
        risk_badge.text = f"⚠️ CRITICAL DRIFT: {risk_score:.2f}"
        risk_badge.style('background-color: #FF007F; color: white; border: 2px solid white')
    else:
        risk_badge.text = f"✅ SECURE: {risk_score:.2f}"
        risk_badge.style('background-color: #00FFC8; color: #0E1117')

# Trigger the chart to draw immediately and refresh every 3 seconds
ui.timer(1.0, update_dashboard)

ui.run(title='Hybrid Behavioral Hackathon', port=9999, reload=False)