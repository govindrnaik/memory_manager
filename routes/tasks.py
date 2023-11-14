from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import SessionLocal, TaskTable, get_db
from sqlalchemy.orm import Session

from models import TaskModel

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Endpoint to create a task
@router.post("/task/", response_model=TaskModel)
def create_task(task: TaskModel, db: Session = Depends(get_db)):
    db_task = TaskTable(**task.dict())
    db.add(instance=db_task)
    db.commit()
    db.refresh(db_task)
    return task

@router.get("/tasks/{task_id}")
async def read_task(task_id: int = 1, db: Session = Depends(get_db)):
    print(task_id)
    task = db.query(TaskTable).filter(TaskTable.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}")
async def update_task(task_id: int, task: TaskModel, db: Session = Depends(get_db)):
    old_task = db.query(TaskTable).filter(TaskTable.id == task_id).first()

    if old_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update the existing task
    for key, value in task.dict().items():
        setattr(old_task, key, value)

    db.commit()
    db.refresh(old_task)
    return old_task

@router.get("/tasks/")
async def read_tasks(skip: int = 0, limit: int = 10):
    tasks = SessionLocal().query(TaskTable).offset(skip).limit(limit).all()
    return tasks

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskTable).filter(TaskTable.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return task

@router.get("/tasks/", response_model=List[TaskModel])
def get_all_tasks(db: Session = Depends(dependency=get_db)):
    tasks = db.query(TaskTable).all()
    print(tasks)
    return tasks

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(dependency=get_db)):
    tasks = db.query(TaskTable).all()
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": tasks})
