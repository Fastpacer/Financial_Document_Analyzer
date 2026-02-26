from fastapi import FastAPI, UploadFile, File, Form
import os
import uuid
from crewai import Crew, Process
from app.agents import financial_analyst
from app.task import analyze_financial_document
from app.database import engine
from app.models import Base
from app.crud import save_result, get_result

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Financial Document Analyzer")


def run_crew(query: str, file_path: str):
    crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential,
    )

    result = crew.kickoff({
        "query": query,
        "file_path": file_path
    })

    return result


@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    query: str = Form("Provide financial insights")
):
    os.makedirs("data", exist_ok=True)

    file_id = str(uuid.uuid4())
    file_path = f"data/{file_id}.pdf"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Run analysis synchronously
    result = run_crew(query, file_path)

    # Save to DB
    record_id = save_result(file.filename, query, str(result))

    # Clean file
    if os.path.exists(file_path):
        os.remove(file_path)

    return {
        "record_id": record_id,
        "analysis": str(result)
    }


@app.get("/result/{record_id}")
def fetch_result(record_id: int):
    record = get_result(record_id)
    if not record:
        return {"status": "Not Found"}

    return {
        "filename": record.filename,
        "query": record.query,
        "analysis": record.result
    }