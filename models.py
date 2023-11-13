from pydantic import BaseModel

class TaskModel(BaseModel):
    title: str
    description: str

class TaskExisted(BaseModel):
    id: int
    title: str
    description: str

class User(BaseModel):
    username: str
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False