from fastapi import FastAPI
from routes.tasks import router as tasks

app = FastAPI()

app.include_router(router=tasks)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0",reload=True, port=8000)