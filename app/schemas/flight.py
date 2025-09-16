from pydantic import BaseModel, ConfigDict
from datetime import datetime

class FlightReportCreate(BaseModel):
    flight_number: str
    airline: str
    departure: str
    arrival: str
    report_text: str

class FlightReportUpdate(BaseModel):
    flight_number: str | None = None
    airline: str | None = None
    departure: str | None = None
    arrival: str | None = None
    report_text: str | None = None

class FlightReportOut(BaseModel):
    model_config = ConfigDict(from_attributes = True)

    id: int
    flight_number: str
    airline: str
    departure: str
    arrival: str
    report_text: str
    created_at: datetime
    user_id: int
