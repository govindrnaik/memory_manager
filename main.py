from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
from typing import List

tasks = []
@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    return tasks[task_id]

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    tasks[task_id] = task
    return task

@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    deleted_task = tasks.pop(task_id)
    return deleted_task

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)