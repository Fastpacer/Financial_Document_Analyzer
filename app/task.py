from crewai import Task
from app.agents import financial_analyst

analyze_financial_document = Task(
    description=(
        "Read the financial document located at {file_path}. "
        "Extract key financial metrics such as revenue, net income, margins, "
        "debt levels, and forward guidance.\n\n"
        "Provide structured analysis:\n"
        "1. Executive Summary\n"
        "2. Financial Performance\n"
        "3. Key Risks\n"
        "4. Investment Outlook\n\n"
        "Base your analysis strictly on the document."
    ),
    expected_output="Structured financial analysis grounded strictly in document content.",
    agent=financial_analyst,
    async_execution=False
)