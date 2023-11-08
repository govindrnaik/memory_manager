from fastapi import FastAPI
from routes.tasks import router as tasks
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from models import Task

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": tasks})

@app.post("/update_task/{task_id}")
async def update_task(task_id: int, task: Task):
    # Update the task description (you can replace this with your logic)
    # For demonstration purposes, we'll just return the updated task
    updated_task = task
    return HTMXResponse(updated_task, template="tasks.html", selector=f"#task-{task_id}")



app.include_router(router=tasks)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0",reload=True, port=8000)