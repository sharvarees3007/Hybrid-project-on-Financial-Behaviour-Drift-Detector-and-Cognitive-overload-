from secure_engine import get_mock_context
import time

def response_engine(secure_report):
    """
    This is the ACTOR. It looks at the secured data and
    decides on a cognitive intervention without knowing the user's name.
    """
    print("\n[🎬 AGENTIC RESPONSE ENGINE STARTING]")
    time.sleep(1)

    # Logic-based decision making (Agentic Behavior)
    if "Severe Drift" in secure_report or "Declining" in secure_report:
        intervention = "🚨 HIGH PRIORITY: Triggering local focus-lock protocol and suggesting a 5-minute mindfulness break."
    elif "Moderate" in secure_report:
        intervention = "⚠️ MEDIUM PRIORITY: Reducing non-essential notifications to stabilize focus."
    else:
        intervention = "✅ LOW PRIORITY: User state stable. Continuing background monitoring."

    return intervention

if __name__ == "__main__":
    print("=== COGNIGUARD SYSTEM END-TO-END FLOW ===")
    
    # 1. Get the secured context
    secure_data_summary = get_mock_context()
    
    # 2. Pass it to the Response Engine
    action = response_engine(secure_data_summary)
    
    print("\n" + "="*50)
    print("FINAL AGENTIC DECISION:")
    print(action)
    print("="*50)
    print("\n[✔] End-to-End Governance & Action Demo Complete.")

    # --- THE LOGGING PART (Must be indented 4 spaces!) ---
    try:
        with open("governance_audit.txt", "a", encoding="utf-8") as f:
            log_time = time.ctime()
            f.write(f"[{log_time}] {secure_data_summary}\n")
            f.write(f"DECISION: {action}\n")
            f.write("-" * 30 + "\n")
        print("\n[📁] Audit Log updated: governance_audit.txt")
    except Exception as e:
        print(f"\n[⚠️] Could not update Audit Log: {e}")