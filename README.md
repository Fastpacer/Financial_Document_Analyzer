# 📊 Financial Document Analyzer
## 🚀 AI Internship Assignment Submission
### 🎯 Objective
Debug and productionize an intentionally broken CrewAI-based financial document analysis system.


### ▶️ How to Run the Application (Step-by-Step)
🖥 System Requirements

Python 3.10 or higher

pip

Groq API Key (Free Tier Supported)

1️⃣ Clone the Repository
git clone <your_repository_url>
cd Financial_Document_Analyzer
2️⃣ Create & Activate Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
macOS / Linux
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
pip install litellm
4️⃣ Configure Environment Variables

Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here

Or set temporarily in terminal:

Windows
set GROQ_API_KEY=your_groq_api_key_here
macOS / Linux
export GROQ_API_KEY=your_groq_api_key_here
5️⃣ Run Backend (FastAPI)
uvicorn app.main:app --reload

Backend will start at:

http://127.0.0.1:8000

You can verify API docs at:

http://127.0.0.1:8000/docs
6️⃣ Run Frontend (Streamlit)

Open a new terminal (keep backend running):

streamlit run frontend/streamlit_app.py

Frontend will open in browser automatically.

### 🧪 How to Test the Application

Upload any financial PDF document

Provide an optional analysis query

Click Analyze Document

View structured

## 📌 Project Overview
This project is a production-ready financial document analysis system built using:

FastAPI (Backend API)

CrewAI (Agent orchestration)

Groq LLM via LiteLLM

SQLite (SQLAlchemy ORM)

Streamlit (Frontend Demo UI)

The original repository contained:

Deterministic runtime bugs

Incorrect tool definitions

Invalid LLM configuration

Inefficient prompt design

Token overflow issues

Broken database integration

✅ All identified issues have been resolved and the system has been refactored into a stable, production-grade architecture.

## 🧠 System Architecture
Code
Streamlit Frontend
        ↓
FastAPI Backend
        ↓
CrewAI Agent
        ↓
Groq LLM (LiteLLM Router)
        ↓
SQLite Database
🛠 Bugs Identified & Fixes Implemented
1️⃣ Tool Validation Error (CrewAI + Pydantic)
❌ Problem: Raw function was passed as a tool.

python
tools=[FinancialDocumentTool.read_data_tool]
✅ Fix: Refactored tool to inherit from BaseTool.

python
class FinancialDocumentTool(BaseTool):
    ...
tools=[FinancialDocumentTool()]
2️⃣ OpenAI API Key Error
❌ Problem: CrewAI defaulted to OpenAI provider internally.
Error: OPENAI_API_KEY is required

✅ Fix: Switched to official CrewAI LLM wrapper.

python
llm = LLM(model="groq/llama3-8b-8192")
Environment variable: GROQ_API_KEY

3️⃣ LiteLLM Fallback Error
❌ Problem: Fallback to LiteLLM not available.
✅ Fix: Installed dependency:

bash
pip install litellm
4️⃣ Incorrect Model (Whisper Used for Chat)
❌ Problem: whisper-large-v3-turbo does not support chat completions.
✅ Fix: Replaced with valid Groq chat model:
groq/llama3-8b-8192

5️⃣ Groq Token Rate Limit (TPM Overflow)
❌ Problem: Full PDF passed to LLM → exceeded 10k tokens/min.
Error: RateLimitError: Requested 12588 tokens

✅ Fix (Production Decision):

python
MAX_CHARS = 8000
full_text = full_text[:MAX_CHARS]
🎯 Tradeoff:

Prevents token overflow

Free-tier compatible

Avoids complex chunking/RAG

6️⃣ SQLAlchemy Import Error
❌ Problem: AnalysisResult model missing.
✅ Fix: Proper ORM model created.

python
class AnalysisResult(Base):
    ...
7️⃣ Celery + Redis Instability (Windows)
❌ Problem: Celery worker failed repeatedly, Redis setup complex.
🎯 Decision: Removed Celery → synchronous processing.

## Tradeoff:

Stability > unnecessary concurrency

Focused on core assignment objectives

Reduced operational complexity

✨ Prompt Engineering Improvements
Original prompts encouraged:

Hallucinations

Fake URLs

Contradictions

Non-compliant financial advice

✅ Refactored Agent Prompt:

Evidence-based analysis only

Structured output

No speculative investment claims

Professional tone

## 📂 Final Repository Structure
Code
Financial_Document_Analyzer/
│
├── app/
│   ├── main.py
│   ├── agents.py
│   ├── task.py
│   ├── tools.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│
├── frontend/
│   └── streamlit_app.py
│
├── analysis.db
├── requirements.txt
└── README.md
⚙️ Setup Instructions
1️⃣ Clone Repository

bash
git clone <your_repo_url>
cd Financial_Document_Analyzer
2️⃣ Create Virtual Environment

bash
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies

bash
pip install -r requirements.txt
pip install litellm
4️⃣ Set Groq API Key  
Create .env file:

Code
GROQ_API_KEY=your_groq_key_here
5️⃣ Run Backend

bash
uvicorn app.main:app --reload
6️⃣ Run Frontend

bash
streamlit run frontend/streamlit_app.py
🔌 API Documentation
POST /analyze
Uploads PDF and returns analysis.

Request:

file: PDF file

query: Optional analysis prompt

Response:

json
{
  "record_id": 1,
  "analysis": "Structured financial analysis..."
}
GET /result/{record_id}
Fetch stored analysis result.

## 🎯 Key Design Choices
Challenge	Decision	Reason
LLM Provider	Groq	Free-tier compatible
Token Overflow	Truncation	Simplicity & reliability
Background Jobs	Removed	Stability under time constraint
Database	SQLite	Lightweight + sufficient
Frontend	Streamlit	Fast demo-ready UI
🧩 Constraints Encountered
Groq free-tier TPM limits

CrewAI strict tool validation

LiteLLM dependency requirement

Windows Redis incompatibility

Model compatibility issues

✅ All were resolved systematically.
