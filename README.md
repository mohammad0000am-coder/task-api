# Task API

A simple REST API built with **FastAPI** and **SQLite** that allows users to create, read, update, and delete tasks.

## Features

- Create tasks
- Read all tasks
- Read a task by ID
- Update tasks
- Delete tasks
- Store data permanently using SQLite

## Technologies

- Python
- FastAPI
- SQLite
- Uvicorn

## Why SQLite?

SQLite was chosen because it is lightweight, requires no separate server, and stores all data in a single database file.

It is suitable for learning backend development and building small applications.

## Database

The application automatically creates a SQLite database named:
```bash
tasks.db
```
When the application starts:

- The database is created if it does not exist.
- The `tasks` table is created automatically.
- Three example tasks are inserted only if the table is empty.

## Project Structure
```bash
task-api/
│
├── images/
│   └── database.png
│
├── main.py
├── tasks.db
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### Clone the repository
```bash
git clone https://github.com/mohammad0000am-coder/task-api.git
```

### Move into the project
```bash
cd task-api
```

### Create a virtual environment
```bash
python -m venv venv
```

### Activate the environment (Windows)
```bash
.\venv\Scripts\Activate.ps1
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the server
```bash
uvicorn main:app --reload
```
## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Returns API information |
| GET | `/health` | Checks if the API is running |
| GET | `/tasks` | Returns all tasks |
| GET | `/tasks/{task_id}` | Returns a single task by ID |
| POST | `/tasks` | Creates a new task |
| PUT | `/tasks/{task_id}` | Updates an existing task |
| DELETE | `/tasks/{task_id}` | Deletes a task |

### Example SQL Query
```bash
SELECT * FROM tasks WHERE done = 1;
```
This query returns all completed tasks.

### Database Screenshot

The database was inspected using DB Browser for SQLite.

![Database Screenshot](images/database.png)

```markdown
## Error Handling

The API handles invalid requests and unknown task IDs:

- `400 Bad Request` is returned for invalid input.
- `404 Not Found` is returned when a task does not exist.

### API Documentation
After running the server, open:
```bash
http://127.0.0.1:8000/docs
```
This opens the interactive Swagger UI documentation.
### Author
Mohammad