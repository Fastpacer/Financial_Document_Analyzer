from app.database import SessionLocal
from app.models import AnalysisResult

def save_result(filename, query, result):
    db = SessionLocal()
    record = AnalysisResult(
        filename=filename,
        query=query,
        result=result
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    db.close()
    return record.id


def get_result(record_id):
    db = SessionLocal()
    record = db.query(AnalysisResult).filter(
        AnalysisResult.id == record_id
    ).first()
    db.close()
    return record