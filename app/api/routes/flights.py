from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.flight import FlightReportCreate, FlightReportOut, FlightReportUpdate
from app.db.session import get_db
from app.crud.flight import (
    create_flight_report,
    get_flight_report,
    get_flight_reports,
    update_flight_report,
    delete_flight_report
)
from app.api.deps import get_current_user

router = APIRouter(prefix="/flights", tags=["flights"])

@router.post("/", response_model=FlightReportOut)
def create_report(report: FlightReportCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return create_flight_report(db, report, current_user.id)

@router.get("/", response_model=list[FlightReportOut])
def list_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_flight_reports(db, skip, limit)

@router.get("/{report_id}", response_model=FlightReportOut)
def get_report(report_id: int, db: Session = Depends(get_db)):
    report = get_flight_report(db, report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@router.put("/{report_id}", response_model=FlightReportOut)
def update_report(report_id: int, report_update: FlightReportUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    report = get_flight_report(db, report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    if report.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this report")
    return update_flight_report(db, report_id, report_update)

@router.delete("/{report_id}", response_model=dict)
def delete_report(report_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    report = get_flight_report(db, report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    if report.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this report")
    delete_flight_report(db, report_id)
    return {"detail": "Report deleted"}
