from fastapi import FastAPI
from pydantic_models1 import Task

app = FastAPI()
tasks: list[Task] = []


@app.get("/")
async def index():
    return tasks


@app.post('/tasks/')
async def create_task(task: Task):
    tasks.append(task)
    return task


@app.put('/task/{task_id}')
async def update_task(task_id: int, new_task: Task):
    filtered_tasks = [task for task in tasks if task.id == task_id]
    if not filtered_tasks:
        return {'update': False}

    task = filtered_tasks[0]
    task.title = new_task.title
    task.description = new_task.description
    task.status = new_task.status

    return {'updated': True, 'task': new_task}


@app.delete('/task/{task_id}')
async def delete_task(task_id: int):
    filtered_tasks = [task for task in tasks if task.id == task_id]
    if not filtered_tasks:
        return {'deleted': False}

    task = filtered_tasks[0]
    tasks.remove(task)
    return {'deleted': True, 'task': task}
