from pydantic import BaseModel

class TaskModel(BaseModel):
    title: str
    description: str
    status: bool

class User(BaseModel):
    username: str
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False