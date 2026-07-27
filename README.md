# Task API

A simple REST API built using FastAPI.

## Features

- Create tasks
- Read tasks
- Update tasks
- Delete tasks

## Technologies

- Python
- FastAPI
- Uvicorn

## Run the project

Create virtual environment:
```bash
python -m venv venv
```
Activate environment:

Windows:
```bash

.\venv\Scripts\Activate.ps1
```
Install dependencies:
```bash

pip install -r requirements.txt
```
Run server:
```bash

uvicorn main:app --reload
```
## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs
## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get one task |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

<img width="1494" height="593" alt="image" src="https://github.com/user-attachments/assets/dd2e4e93-2265-453c-8ceb-13466d12df5a" />
