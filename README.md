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
   (Assuming your Python file is named main.py)

   This will start the FastAPI application on http://127.0.0.1:8000.

---

## API Endpoints

You can interact with the API using tools like curl or a dedicated API testing tool like Postman or Insomnia.

1. GET /
     Redirects to the API documentation.

2. POST /tasks/
     Creates a new task.

Request Body :

JSON

{
    "title": "Buy groceries",
    "description": "Milk, eggs, bread, and cheese",
    "completed": false
}

Response Body (Success - 200 OK): The newly created task with its assigned ID.

GET /tasks/

