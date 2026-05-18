# Healthcare Management Backend System

A modular Healthcare Management Backend System built using FastAPI and PostgreSQL.

## Live Deployment

### Live API
https://healthcare-backend-system-avwn.onrender.com

### Swagger API Documentation
https://healthcare-backend-system-avwn.onrender.com/docs

---

# Tech Stack

- Python
- FastAPI
- PostgreSQL
- psycopg2
- Pydantic
- Uvicorn
- Render Cloud Deployment

---

# Features

- Modular FastAPI architecture
- PostgreSQL relational database integration
- Patients management APIs
- Doctors management APIs
- Illness management APIs
- Appointment management APIs
- Middleware logging
- Global exception handling
- Request and response validation using Pydantic
- Cloud PostgreSQL integration
- Public API deployment

---

# Project Structure

```bash
healthcare_backend/
│
├── main.py
├── routers/
├── schemas/
├── middleware/
├── exceptionHandlers/
├── db/
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Database Schema

## illnesses

| Column | Type |
|---|---|
| id | SERIAL PRIMARY KEY |
| illness | VARCHAR(100) |

## patients

| Column | Type |
|---|---|
| id | SERIAL PRIMARY KEY |
| patient_name | VARCHAR(100) |
| illness_id | INT |

## doctors

| Column | Type |
|---|---|
| id | SERIAL PRIMARY KEY |
| doctor_name | VARCHAR(100) |
| specialization | VARCHAR(100) |

## appointments

| Column | Type |
|---|---|
| id | SERIAL PRIMARY KEY |
| patient_id | INT |
| doctor_id | INT |
| date | DATE |
| time | TIME |
| status | VARCHAR(50) |

---

# API Endpoints

## Patients
- POST /patients
- GET /patients

## Doctors
- POST /doctors
- GET /doctors

## Illnesses
- POST /illnesses
- GET /illnesses

## Appointments
- POST /appointments
- GET /appointments

---

# Middleware

- Request logging
- Execution time tracking

---

# Exception Handling

Global exception handling implemented using:
- HTTPException
- JSONResponse

---

# Cloud Deployment

Deployed publicly using Render with:
- cloud-hosted FastAPI backend
- cloud PostgreSQL database
- environment variables for secure DB configuration

---

# Environment Variables

```env
DATABASE_URL=your_render_postgresql_internal_database_url
```

---

# Installation & Local Setup

## Create Virtual Environment

```bash
python -m venv env
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run FastAPI Server

```bash
uvicorn main:app --reload
```

---

# Author

Giri Venkatesh
