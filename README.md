# FastAPI Patient Management System

A beginner-friendly backend API project built using FastAPI.

## Features

* View all patients
* View single patient
* Create patient
* Delete patient
* Sort patients
* Path Parameters
* Query Parameters
* Exception Handling
* JSON-based database

---

## Tech Stack

* Python
* FastAPI
* JSON
* Uvicorn

---

## Installation

Clone the repository:

```bash
git clone https://github.com/dhii24/fastapi-patient-management-system.git
```

Move into project folder:

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
| POST   | `/create/{patient_id}`  | Create patient      |
| DELETE | `/delete/{patient_id}`  | Delete patient      |

---

## Sample Create Request

```json
{
  "name": "Dhiraj",
  "age": 23,
  "height": 183,
  "weight": 74,
  "bmi": 22.1
}
```

---

## Future Improvements

* Update Patient API
* MongoDB Integration
* JWT Authentication
* Docker Support
* Deployment on Render

---

## Author

Dhiraj Acharya
