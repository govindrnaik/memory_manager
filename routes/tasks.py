from typing import List
from fastapi import APIRouter

from models import Task

router = APIRouter()

tasks = []
@router.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    tasks.routerend(task)
    return task

@router.get("/tasks/", response_model=List[Task])
async def read_tasks():
    return tasks

@router.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    return tasks[task_id]

@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    tasks[task_id] = task
    return task

@router.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    deleted_task = tasks.pop(task_id)
    return deleted_task