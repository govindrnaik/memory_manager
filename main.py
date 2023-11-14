from fastapi import FastAPI
from routes.tasks import router as tasks
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(router=tasks)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0",reload=True, port=8000)
