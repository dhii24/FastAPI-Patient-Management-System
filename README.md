# FastAPI Patient Management System

A beginner-friendly backend API project built using FastAPI for managing patient records. The project demonstrates CRUD operations, request validation, query parameters, exception handling, and automatic BMI calculation using Pydantic models.

## Features

* View all patients
* View single patient
* Create patient
* Update patient
* Delete patient
* Sort patients by height, weight, or BMI
* Path Parameters
* Query Parameters
* Request Validation with Pydantic
* Exception Handling
* Automatic BMI Calculation
* Automatic Health Verdict Generation
* JSON-based data storage

---

## Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn
* JSON

---

## Installation

Clone the repository:

```bash
git clone https://github.com/dhii24/fastapi-patient-management-system.git
```

Navigate to the project directory:

```bash
cd fastapi-patient-management-system
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

---

## Run the Project

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Redoc:

```text
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

| Method | Endpoint                | Description         |
| ------ | ----------------------- | ------------------- |
| GET    | `/`                     | Home route          |
| GET    | `/about`                | About API           |
| GET    | `/view`                 | View all patients   |
| GET    | `/patient/{patient_id}` | View single patient |
| GET    | `/sort`                 | Sort patients       |
| POST   | `/create`               | Create patient      |
| PUT    | `/edit/{patient_id}`    | Update patient      |
| DELETE | `/delete/{patient_id}`  | Delete patient      |

---

## Sample Create Request

```json
{
  "id": "P008",
  "name": "Dhiraj Acharya",
  "city": "Bangalore",
  "age": 23,
  "gender": "male",
  "height": 1.83,
  "weight": 74
}
```

---

## Validations Implemented

* Age must be between 1 and 119
* Height must be greater than 0
* Weight must be greater than 0
* Gender validation using Literal
* Automatic BMI calculation using computed fields
* Automatic health verdict generation based on BMI

---

## Future Improvements

* SQLite Integration
* PostgreSQL Integration
* SQLAlchemy ORM
* JWT Authentication
* Docker Support
* Deployment on Render
* Unit Testing with Pytest

---

## Author

Dhiraj Acharya
