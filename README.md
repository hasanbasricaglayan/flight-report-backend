# Flight-Report.com Backend

A **FastAPI backend** for a Flight Report platform where users can register, log in, create flight reports, and comment on reports. This project is fully containerized with Docker and uses **SQLAlchemy ORM**, **JWT authentication** and **PostgreSQL**.

## Features

- User registration and login (JWT authentication)
- Create, read, update, delete (CRUD) flight reports
- Add, read, update, delete comments on flight reports
- Automatic table creation with SQLAlchemy
- Environment variable management via `.env`
- Dockerized for easy deployment


## Requirements

- Python 3.12+ (if running locally)
- Docker & Docker Compose


## Environment Variables

| Variable | Description |
| --- | --- |
| POSTGRES_USER | PostgreSQL username |
| POSTGRES_PASSWORD | PostgreSQL password |
| POSTGRES_DB | PostgreSQL database name |
| DATABASE_URL | SQLAlchemy connection URL |
| SECRET_KEY | JWT secret key |
| ACCESS_TOKEN_EXPIRE_MINUTES | JWT expiration time in minutes |


## Setup

Create a `.env` file in the root directory of the project. Add environment variables on new lines in the form of `NAME=VALUE`. For example:

```
POSTGRES_USER=flightuser
POSTGRES_PASSWORD=flightpass
POSTGRES_DB=flightdb
DATABASE_URL=postgresql+psycopg2://flightuser:flightpass@db:5432/flightdb
SECRET_KEY=thisisthekeyforflightreportcloneproject
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

### With Docker

1. Build and start containers:

```bash
docker-compose up --build
```

2. FastAPI will be available at:

```
http://localhost:8000
```

### Without Docker

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Ensure `.env` exists and run:

```bash
uvicorn app.main:app --reload
```

4. FastAPI will be available at:

```
http://localhost:8000
```
