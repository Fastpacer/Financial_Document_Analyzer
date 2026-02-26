import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from app.tools import FinancialDocumentTool

load_dotenv()

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.2
)

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents and provide evidence-based investment insights.",
    backstory=(
        "You are a CFA-certified financial analyst with 15+ years of experience. "
        "You strictly rely on document evidence and avoid speculation."
    ),
    tools=[FinancialDocumentTool()],
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=False
)