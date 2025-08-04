# FastAPI Task Management API

This is a simple task management API built using FastAPI. It allows you to perform basic CRUD (Create, Read, Update, Delete) operations on a list of tasks.

---

## Features

   1. Create Task: Add a new task with a title, optional description, and completion status.
   
   2. Read Tasks: Retrieve a list of all tasks.

   3. Read Single Task: Retrieve details of a specific task using its unique ID.
   
   4. Update Task: Modify the title, description, or completion status of an existing task.  
   
   5. Delete Task: Remove a specific task using its unique ID.

---

## Technologies Used

  1. FastAPI: A modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
  
  2. Pydantic: Data validation and settings management using Python type annotations.
  
  3. UUID: Universally unique identifiers for task identification.
  
  4. Uvicorn: A lightning-fast ASGI server for running FastAPI applications.  

---

## Getting Started

1. Clone the repository (if you have it in one).

2. Install dependencies:
```Bash

    pip install fastapi uvicorn

```

3. Run the application:

```Bash

   python main.py

```
   --> (Assuming your Python file is named main.py)

   --> This will start the FastAPI application on http://127.0.0.1:8000 .

---

## API Endpoints

You can interact with the API using tools like curl or a dedicated API testing tool like Postman or Insomnia.

--> GET /
     Redirects to the API documentation.

1. POST /tasks/
     Creates a new task.

     Request Body :

     JSON
```bash
{
    "title": "Buy groceries",
    "description": "Milk, eggs, bread, and cheese",
    "completed": false
}
```
--> Response Body (Success - 200 OK): The newly created task with its assigned ID.

2. GET /tasks/

   Retrieves a list of all tasks.
   --> Response Body (Success - 200 OK): A JSON array of task objects.


   GET /tasks/{task_id}
   Retrieves a specific task by its ID.
   Path Parameter: task_id (UUID)
   --> Response Body (Success - 200 OK): The requested task object.
   --> Response (Error - 404 Not Found): If the task with the given ID does not exist.

3. PUT /tasks/{task_id}
   Updates an existing task
   Path Parameter: task_id (UUID)
   --> Request Body: The task data to update (only the fields you want to change are necessary).

JSON

{
    "title": "Buy groceries for the week",
    "completed": true
}

--> Response Body (Success - 200 OK): The updated task object.
--> Response (Error - 404 Not Found): If the task with the given ID does not exist.


4. DELETE /tasks/{task_id}
   Deletes a specific task by its ID.
   Path Parameter: task_id (UUID)

--> Response Body (Success - 200 OK): The deleted task object.
   --> Response (Error - 404 Not Found): If the task with the given ID does not exist.

---
## This code demonstrates the creation of a basic RESTful API using FastAPI to manage a collection of tasks.

--> API Endpoints: created routes for the root path (/) which redirects to the documentation, and for the /tasks/ path to handle creating, reading (all and single), updating, and deleting tasks.

--> Implemented CRUD Operations: You've implemented the fundamental Create, Read, Update, & Delete operations for tasks
    using the corresponding HTTP methods (POST, GET, PUT, DELETE).

--> Used Pydantic for Data Modeling and Validation: You've defined the Task Pydantic model to structure the task data,
    including its ID (optional on creation), title, optional description, and completion status. Pydantic automatically
    handles data validation based on this model.

--> Utilized UUIDs for Unique Identification: Each new task is assigned a unique ID using the uuid4() function,
    ensuring that each task can be uniquely identified.

--> Implemented Basic Error Handling: You've used HTTPException to return a 404 Not Found error when a request is made for a task that doesn't exist.

--> Managed Data in Memory: The tasks list serves as an in-memory data store for the tasks. This means the data will be lost when the application restarts.
    For a production application, you would typically integrate with a persistent database.

--> Leveraged FastAPI Features: You've utilized FastAPI's decorators (@app.get, @app.post, @app.put, @app.delete), path parameters ({task_id}), request body    
    handling, and response model definition (response_model).

--> Provided API Documentation : FastAPI automatically generates interactive API documentation (using Swagger UI) accessible at /docs and alternative
    documentation (using ReDoc) at /redoc.

--> This code provides a foundational understanding of building RESTful APIs with FastAPI and demonstrates essential concepts like routing, data modeling, request handling, and basic error management.
