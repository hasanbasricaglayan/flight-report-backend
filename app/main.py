from fastapi import FastAPI
from app.db.session import engine, Base
from app.api.routes import users, flights, comments

# Create all tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Flight-Report.com Clone")

app.include_router(users.router, prefix="/api")
app.include_router(flights.router, prefix="/api")
app.include_router(comments.router, prefix="/api")
