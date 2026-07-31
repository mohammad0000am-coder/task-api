# reloading the server : uvicorn main:app --reload
# activating the environment : .\venv\Scripts\Activate.ps1
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    done: bool
tasks = [
    {
        "id": 1,
        "title": "Study FastAPI",
        "done": False
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
    },
    {
        "id": 4,
        "title": "Practice API",
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
    return tasks

@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

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
