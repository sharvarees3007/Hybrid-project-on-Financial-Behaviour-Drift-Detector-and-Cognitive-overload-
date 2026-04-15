import random
import time

def get_mock_context():
    # These are the exact values you provided
    mock_database = [
        {"name": "Amit", "focus": 8, "distractions": 1, "action": "study", "status": "Stable"},
        {"name": "Neha", "focus": 4, "distractions": 6, "action": "distraction", "status": "Declining"},
        {"name": "Rahul", "focus": 2, "distractions": 10, "action": "idle", "status": "Severe Drift"},
        {"name": "Sneha", "focus": 5, "distractions": 4, "action": "switch_task", "status": "Moderate"},
        {"name": "Arjun", "focus": 4, "distractions": 7, "action": "distraction", "status": "Rising Distraction"}
    ]
    
    # Simulating the 'SELECT' query
    data = random.choice(mock_database)
    
    print("---  FETCHING FROM BEHAVIOUR_LOGS (MOCK) ---")
    time.sleep(0.8) 
    
    # Formatting the data for the AI 'Brain'
    context = (f"The user ({data['name']}) currently has a Focus Score of {data['focus']}/10. "
               f"Distraction count is {data['distractions']} and their last recorded action was '{data['action']}'. "
               f"The system characterizes this as {data['status']}.")
    
    return context

if __name__ == "__main__":
    print("\n=== COGNIGUARD BEHAVIOURAL DRIFT ENGINE ===")
    ai_context = get_mock_context()
    print("-" * 50)
    print("RAW DATA CONTEXT FOR AI:")
    print(ai_context)
    print("-" * 50)