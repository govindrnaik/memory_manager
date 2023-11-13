from typing import List
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import SessionLocal, TaskTable, get_db
from models import TaskExisted, TaskModel
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("/tasks/", response_model=List[TaskModel])
async def read_tasks(skip: int = 0, limit: int = 10):
    tasks = SessionLocal().query(TaskTable).offset(skip).limit(limit).all()
    return tasks


# @router.post("/tasks/", response_model=Task)
async def create_task(title: str, description: str, db: Session = Depends(get_db)):
    new_task = TaskModel(title=title, description=description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.get("/tasks/{task_id}")
async def read_task(task_id: int, db: Session = Depends(get_db)):
    print(task_id)
    task = db.query(TaskTable).filter(TaskExisted.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=TaskModel)
async def update_task(task_id: int, task: TaskModel, db: Session = Depends(get_db)):
    task = db.query(TaskTable).filter(TaskModel.id == task_id).first()
    return task

@router.delete("/tasks/{task_id}", response_model=TaskModel)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskExisted).filter(TaskExisted.id == task_id).first()
    db.delete(task)
    db.commit()
    return task

@router.get("/tasks/", response_model=List[TaskModel])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(TaskTable).all()
    return tasks

# Endpoint to create a task
@router.post("/tasks/", response_model=TaskModel)
def create_task(task: TaskModel, db: Session = Depends(get_db)):
    print(task.dict())
    db_task = TaskTable(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return task
