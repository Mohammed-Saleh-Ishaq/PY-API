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
# This will allow us to Read an individual task based on its ID.
@app.get("/tasks/{task_id}", response_model= Task)
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code = 404, detail = "Task not Found" )

# Update/Put method/ request
@app.put("/tasks/{task_id}", response_model= Task)
def update_task(task_id: UUID , task_update: Task):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            update_task = task.copy(update = task_update.dict(exclude_unset= True))
            tasks[idx]=update_task
            return update_task
    raise HTTPException(status_code = 404, detail = "Task not Found" )



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)