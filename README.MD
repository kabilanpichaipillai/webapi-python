## WebAPI using Python FastAPI

- Welcome endpoint
- Create, Read, Update, Delete (CRUD) users
- Input validation using Pydantic
- In-memory database (demo purpose)
- Swagger UI & ReDoc
- Automated API tests (TDD)
- Docker support

---

## Project Structure

fastapi-app/
│
├── main.py # FastAPI application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
├── README.md # Project documentation
└── tests/
├── init.py
└── test_users.py # Automated tests

---

## Requirements

- Python 3.10+
- Docker (optional)
- pip

---

## Run the application locally

uvicorn main:app --reload

Application will be available at:

API: http://localhost:8000

Welcome API: http://localhost:8000/welcome

Get User: http://localhost:8000/user

Swagger UI: http://localhost:8000/docs

---

## API Endpoints

### Welcome
GET /welcome

### Get default user
GET /user

### Get user by ID
GET /user/{user_id}

### Create user
POST /user

### Update user
PUT /user/{user_id}

### Delete user
DELETE /user/{user_id}

----

## Automated Testing (TDD)

### Run test locally
pytest -v

---

## Docker Support

### Build Docker Image
docker build -t fastapi-user-app .

### Run Container
docker run -d -p 8000:8000 --name fastapi-container fastapi-user-app


