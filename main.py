# reloading the server : uvicorn main:app --reload
# activating the environment : .\venv\Scripts\Activate.ps1
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

def get_connection():
    return sqlite3.connect("tasks.db")

def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        done BOOLEAN NOT NULL
    )
    """)

    connection.commit()
    connection.close()

def insert_initial_tasks():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")

    count = cursor.fetchone()[0]

    if count == 0:

        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            ("Study FastAPI", False)
        )

        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            ("Exercise", True)
        )

        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            ("Read book", False)
        )

    connection.commit()
    connection.close()    

def get_all_tasks():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    connection.close()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "done": bool(row[2])
        })

    return tasks

create_tables()
insert_initial_tasks()

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    done: bool
tasks = [
    {
        "id": 1,
        "title": "Study FastAPI",
        "done": True
    },
    {
        "id": 2,
        "title": "Exercise",
        "done": True
    },
    {
        "id": 3,
        "title": "Read book",
        "done": False
    }
]
@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/tasks")
def get_tasks():
    return get_all_tasks()

@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cursor.fetchone()

    connection.close()

    if row:
        return {
            "id": row[0],
            "title": row[1],
            "done": bool(row[2])
        }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
    
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):

    for item in tasks:
        if item["id"] == task_id:

            item["title"] = task.title
            item["done"] = task.done

            return item

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):

    for index, item in enumerate(tasks):
        if item["id"] == task_id:

            tasks.pop(index)

            return

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )