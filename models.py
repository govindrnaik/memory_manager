from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    status: bool = False


class User(BaseModel):
    username: str
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False