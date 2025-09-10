from sqlalchemy.orm import Session
from app.models.flight import FlightReport
from app.schemas.flight import FlightReportCreate, FlightReportUpdate

def create_flight_report(db: Session, report: FlightReportCreate, user_id: int):
    db_report = FlightReport(**report.dict(), user_id=user_id)
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

def get_flight_report(db: Session, report_id: int):
    return db.query(FlightReport).filter(FlightReport.id == report_id).first()

def get_flight_reports(db: Session, skip: int = 0, limit: int = 10):
    return db.query(FlightReport).offset(skip).limit(limit).all()

def update_flight_report(db: Session, report_id: int, report_update: FlightReportUpdate):
    db_report = db.query(FlightReport).filter(FlightReport.id == report_id).first()
    if db_report:
        for key, value in report_update.dict(exclude_unset=True).items():
            setattr(db_report, key, value)
        db.commit()
        db.refresh(db_report)
    return db_report

def delete_flight_report(db: Session, report_id: int):
    db_report = db.query(FlightReport).filter(FlightReport.id == report_id).first()
    if db_report:
        db.delete(db_report)
        db.commit()
    return db_report
