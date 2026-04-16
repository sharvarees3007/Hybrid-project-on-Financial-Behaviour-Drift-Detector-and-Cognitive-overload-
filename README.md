<div align="center">

<h1>🛡️ CogniGuard</h1>

<p><b>Financial Behaviour Drift Detector & Cognitive Overload System</b></p>

<p><i>Hybrid Data Governance & Privacy-Preserving Agentic Interventions</i></p>

<div>

<img src="https://img.shields.io/badge/Python%203.14-3776AB?logo=python\&logoColor=fff" alt="Python" />

<img src="https://img.shields.io/badge/MySQL-4479A1?logo=mysql\&logoColor=fff" alt="MySQL" />

</div>

</div>

## **🌟 About CogniGuard**

**CogniGuard** is a hybrid, end-to-end data governance and behavioral analysis pipeline designed to proactively monitor cognitive overload and behavioral drift. Optimized for privacy and compliance, this system transforms raw, sensitive user activity logs into secured, actionable insights.

By combining **Differential Privacy** mathematics with an **Agentic Response Engine**, CogniGuard achieves real-time evaluation of user stress levels—triggering automated governance interventions without ever exposing raw Personally Identifiable Information (PII).

## **📍 Project Goals \& Implementation Status**

|Requirement|Status|Technical Implementation|
|-|-|-|
|**Real-Time Data Ingestion**|✅|**Mock Bridge (mock\_bridge.py):** Simulates live behavioral monitoring feeds, extracting focus and distraction metrics.|
|**Privacy \& Anonymization**|✅|**Secure Engine (secure\_engine.py):** Hashes PII (SHA-256) and injects differential privacy noise to protect user identity.|
|**Automated Interventions**|✅|**Action Agent (action\_agent.py):** Agentic response system that evaluates secured data to trigger focus-lock protocols or breaks.|
|**Immutable Auditing**|✅|**SQL \& Local Logging:** Maintains a strict governance trail via governance\_audit.txt and relational database schemas.|

## **✨ Core Features**

* **🕵️‍♂️ Behavioral Drift Detection**: Analyzes focus scores and distraction counts to categorize user cognitive states dynamically (e.g., Stable, Overloaded, Drifted).
* **🛡️ Differential Privacy Shield**: Automatically masks PII using cryptographic hashing and math-based noise injection to prevent identity leakage in analytical views.
* **🤖 Agentic Response Engine**: Autonomous governance actor evaluating sanitized data to recommend interventions (High, Medium, Low priority) without accessing raw identities.
* **📊 Advanced SQL Analytics**: Computes a multi-variable "Total Stress Index" to securely identify critically overloaded users via relational database views.

## **🏗️ System Architecture \& Execution Flow**

While the system operates as a unified pipeline, it is cleanly separated into distinct Python engines and SQL analytical layers to ensure strict data governance.

|Stage|Component|Core Function \& Responsibility|
|-|-|-|
|**1. Ingestion**|mock\_bridge.py|Fetches raw behavioral logs (Name, Focus, Distractions, Actions).|
|**2. Sanitization**|secure\_engine.py|Strips identity (SUB-XXXX), applies differential privacy to scores.|
|**3. Execution**|action\_agent.py|Logic-based decision making for priority interventions and audit logging.|
|**4. Analytics**|HP\_1\_LOGIC.sql|Calculates Hybrid Alerts, Classifications, and Stress Index scoring.|

## **🚀 Getting Started**

### **Prerequisites**

1. **Python 3.8+**
2. **MySQL Server** (for running the analytics schema)
3. Basic understanding of Python virtual environments (recommended).

### **Setup**

1. Clone the repository and navigate to the project directory.
2. Run the complete Agentic Governance flow:  
python action\_agent.py
3. Test individual pipeline components:  
# Test raw data ingestion  
python mock\_bridge.py

   \# Test PII masking \& privacy injection  
python secure\_engine.py

4. Initialize Database Analytics:  
-- Load the schema and baseline tables  
SOURCE database/HP\_1\_Schema.sql;

   \-- Execute the analytical logic views  
SOURCE database/HP\_1\_LOGIC.sql;

   ## **📄 License**

   This project is licensed under the MIT License.

