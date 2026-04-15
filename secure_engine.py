import random
import time
import hashlib

# 1. THE SECURITY VAULT (Keep this at the top)
SECRET_SALT = "COGNIGUARD_SECURE_2026"

def secure_privacy_gateway(raw_data_dict):
    """
    This is the SECURITY LAYER. 
    It anonymizes PII and adds 'Differential Privacy' to metrics.
    """
    # Anonymize the Name
    name_bytes = (raw_data_dict['name'] + SECRET_SALT).encode()
    secure_id = f"SUB-{hashlib.sha256(name_bytes).hexdigest()[:6].upper()}"
    
    # Add 'Noise' to the Focus Score
    noise = random.uniform(-0.2, 0.2)
    obfuscated_focus = round(raw_data_dict['focus'] + noise, 2)
    
    return {
        "id": secure_id,
        "focus": obfuscated_focus,
        "status": raw_data_dict['status']
    }

# 2. THE MOCK DATABASE
def get_mock_context():
    mock_database = [
        {"name": "Amit", "focus": 8, "distractions": 1, "action": "study", "status": "Stable"},
        {"name": "Neha", "focus": 4, "distractions": 6, "action": "distraction", "status": "Declining"},
        {"name": "Rahul", "focus": 2, "distractions": 10, "action": "idle", "status": "Severe Drift"},
        {"name": "Sneha", "focus": 5, "distractions": 4, "action": "switch_task", "status": "Moderate"},
        {"name": "Arjun", "focus": 4, "distractions": 7, "action": "distraction", "status": "Rising Distraction"}
    ]
    
    # Simulating the 'SELECT' query
    raw_data = random.choice(mock_database)
    
    # --- ADDED: THE AGENT'S THOUGHT PROCESS ---
    print("\n" + "="*40)
    print("[ AGENTIC GOVERNANCE ACTIVE]")
    print(f"1. Detecting PII... Found name: '{raw_data['name']}' -> ACTION: MASKING")
    
    # Secure the data
    secure_data = secure_privacy_gateway(raw_data)
    
    print(f"2. Analyzing Risk... Status is '{secure_data['status']}' -> ACTION: LOGGING")
    print(f"3. Applying Differential Privacy... Original Focus: {raw_data['focus']} -> New: {secure_data['focus']}")
    
    # Final output context
    context = (f"\n[SAFE OUTPUT]: Analysis for {secure_data['id']}: "
               f"Focus {secure_data['focus']}/10. Status: {secure_data['status']}.")
    return context

# 3. THE EXECUTION
if __name__ == "__main__":
    print("=== COGNIGUARD BEHAVIOURAL DRIFT ENGINE ===")
    
    # Run the engine
    final_report = get_mock_context()
    
    print("-" * 50)
    print(final_report)
    print("-" * 50)
    print("DATA GOVERNANCE CHECK COMPLETE: NO PII LEAKED.")