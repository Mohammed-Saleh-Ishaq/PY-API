from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID , uuid4


app = FastAPI()

class Task(BaseModel):
    id : Optional[UUID] = None
    title : str
    description : Optional[str] = None
    completed : bool = False

tasks = []
# Create method task .
@app.post("/tasks/", response_model= Task)  
def create_task(task : Task):
    task.id = uuid4()
    tasks.append(task)
    return task

# Get/Read method .
@app.get("/tasks/", response_model=List[Task])  
def read_tasks():
    return tasks

# Path Parameters.
@app.get("/tasks/{task_id}", response_model= Task)
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    return HTTPException(status_code = 404, detail = "Task not Found" )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)