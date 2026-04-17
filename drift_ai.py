import pandas as pd
import numpy as np
import json
import time
from datetime import datetime
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Configuration
ITERATIONS = 30  # Number of events to simulate before stopping
history = []
scaler = StandardScaler()
iso_model = IsolationForest(contamination=0.15, random_state=42)
lr_model = LogisticRegression()

def generate_event():
    return {
        "user_id": np.random.randint(1, 4),
        "difficulty": np.random.uniform(1, 10),
        "pressure": np.random.uniform(1, 10),
        "focus": np.random.uniform(1, 10),
        "distraction": np.random.uniform(1, 10),
        "amount": np.random.uniform(100, 2000),
        "timestamp": str(datetime.now())
    }

def process(event):
    t = pd.to_datetime(event["timestamp"])

    cognitive_load = (0.4 * event["pressure"] +
                      0.3 * event["difficulty"] +
                      0.3 * event["distraction"])

    stability = event["focus"] / (event["distraction"] + 1)
    impulse = event["amount"] / (event["focus"] + 1)
    drift_risk = (0.6 * cognitive_load + 0.4 * impulse)

    return {
        "user_id": event["user_id"],
        "hour": t.hour,
        "day": t.day,
        "cognitive_load": cognitive_load,
        "stability": stability,
        "impulse": impulse,
        "drift_risk": drift_risk,
        "amount": event["amount"]
    }

def train(df):
    if len(df) < 20:
        return False

    X = df[["cognitive_load", "impulse", "stability"]]
    scaler.fit(X)
    X_scaled = scaler.transform(X)

    iso_model.fit(X_scaled)

    y = (df["drift_risk"] > df["drift_risk"].median()).astype(int)
    lr_model.fit(X_scaled, y)

    return True

def patterns(df):
    worst_hour = df.groupby("hour")["amount"].mean().idxmax()
    early = df[df["day"] <= 5]["amount"].mean()
    late = df[df["day"] > 5]["amount"].mean()
    return worst_hour, early > late

def dopamine(df):
    df["spike"] = df["amount"].diff().fillna(0)
    return df["spike"].iloc[-1] > df["spike"].mean() * 2

def generate_psych_actions(insights, current):
    actions = []
    mapping = {
        "High financial drift risk": "You’re not making decisions—you’re reacting. Add a 10-minute delay before any purchase.",
        "Dopamine spending loop": "Your brain is chasing novelty. Change your environment immediately—stand up, walk, reset.",
        "Behavior anomaly": "This behavior deviates from your baseline. Avoid financial decisions for the next hour.",
        "Peak risk hour": "This is your weakest control window. Pre-commit to zero spending during this hour.",
        "Salary cycle overspending": "You associate money with freedom. Lock away a portion immediately to reduce impulse access.",
        "Low cognitive stability": "Your attention is fragmented. Eliminate distractions and force single-tasking for 15 minutes."
    }
    
    for insight in insights:
        if insight in mapping:
            actions.append(mapping[insight])

    if not actions:
        actions.append("Stable state detected. Maintain current behavior.")

    return actions

def analyze(df, current):
    X = df[["cognitive_load", "impulse", "stability"]]
    X_scaled = scaler.transform(X)

    anomaly = iso_model.predict(X_scaled)[-1]
    drift_prob = lr_model.predict_proba(X_scaled)[-1][1]

    worst_hour, salary_spike = patterns(df)
    dop = dopamine(df)

    insights = []
    if anomaly == -1: insights.append("Behavior anomaly")
    if drift_prob > 0.75: insights.append("High financial drift risk")
    if dop: insights.append("Dopamine spending loop")
    if current["hour"] == worst_hour: insights.append("Peak risk hour")
    if salary_spike and current["day"] <= 5: insights.append("Salary cycle overspending")
    if current["stability"] < 0.5: insights.append("Low cognitive stability")

    psych_actions = generate_psych_actions(insights, current)

    return {
        "user_id": current["user_id"],
        "drift_probability": float(drift_prob),
        "insights": insights,
        "psychological_analysis": psych_actions,
        "time": str(datetime.now())
    }

print(f"Cognitive Drift AI starting for {ITERATIONS} cycles...\n")

for i in range(ITERATIONS):
    event = generate_event()
    processed = process(event)
    history.append(processed)

    df = pd.DataFrame(history)

    if not train(df):
        print(f"[{i+1}/{ITERATIONS}] Collecting behavioral data ({len(df)}/20)...")
        time.sleep(0.1) # Faster for testing
        continue

    result = analyze(df, processed)

    print(f"\n--- AI OUTPUT (Cycle {i+1}) ---")
    print(json.dumps(result, indent=2))

    time.sleep(0.5)

print("\nSimulation complete.")
print(f"Final Data points collected: {len(history)}")
