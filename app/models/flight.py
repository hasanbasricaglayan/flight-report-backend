from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime, timezone

class FlightReport(Base):
    __tablename__ = "flight_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    flight_number = Column(String, index=True)
    airline = Column(String)
    departure = Column(String)
    arrival = Column(String)
    report_text = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User")
    comments = relationship("Comment", back_populates="flight_report", cascade="all, delete-orphan")
