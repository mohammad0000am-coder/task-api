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

python -m venv venv

Activate environment:

Windows:
.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn main:app --reload

## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs