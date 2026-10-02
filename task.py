from datetime import datetime
import argparse
import json
from dataclasses import dataclass, asdict
from pprint import pprint

@dataclass
class Task:
    id: int
    description: str
    status: str
    created_at: str
    updated_at: str
    

# parser = argparse.ArgumentParser()

# subparsers = parser.add_subparsers(dest="command")

# add_parser = subparsers.add_parser("add")
# add_parser.add_argument("title")

# list_parser = subparsers.add_parser("list")

# args = parser.parse_args()

# if args.command == "add":
#     print(f"Adding task: {args.title}")

# if args.command == "list":
#     print("Listing tasks..")

# print(args)



# create task 
def add():
    tasks = load_tasks()
    
    new_task = Task(
        1,
        "learn html",
        "done",
        "83",
        "334"
    )
    
    task_dict = asdict(new_task)
    
    tasks.append(task_dict)
    
    save_tasks(tasks)


# update task
def update(task_id, description):
    tasks = load_tasks()
    
    for i in tasks:
        if i["id"] == task_id:
            task = i
    
    task["description"] = description
    
    save_tasks(tasks)
    

# delete task
def delete(task_id):
    tasks = load_tasks()
    
    for i in tasks:
        if i["id"] == task_id:
            tasks.remove(i)
    
    save_tasks(tasks)


# mark a task in progress
def mark_in_progress(task_id):
    tasks = load_tasks()
        
    for i in tasks:
        if i["id"] == task_id:
            task = i
        
    task["status"] = "in-progress"
        
    save_tasks(tasks)


# mark a task done
def mark_done(task_id):
    tasks = load_tasks()
            
    for i in tasks:
        if i["id"] == task_id:
            task = i
            
    task["status"] = "done"
            
    save_tasks(tasks)



# listing all tasks
def task_list():
    tasks = load_tasks()
    
    for task in tasks:
        print(f"id: {task['id']} | description: {task['description']} | status: {task['status']} | created: {task["created_at"]} | updated: {task["updated_at"]}")


# listing done tasks
def task_list_done():
    all_tasks = load_tasks()
    
    for task in all_tasks:
        if task["status"] == "done":
             print(f"id: {task['id']} | description: {task['description']} | status: {task['status']} | created: {task["created_at"]} | updated: {task["updated_at"]}")


# listing todo tasks
def task_list_todo():
    all_tasks = load_tasks()
    
    for task in all_tasks:
        if task["status"] == "todo":
             print(f"id: {task['id']} | description: {task['description']} | status: {task['status']} | created: {task["created_at"]} | updated: {task["updated_at"]}")



# listing in progress tasks
def task_in_progress_tasks():
    all_tasks = load_tasks()
    
    for task in all_tasks:
        if task["status"] == "in-progress":
             print(f"id: {task['id']} | description: {task['description']} | status: {task['status']} | created: {task["created_at"]} | updated: {task["updated_at"]}")



# load task from json file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileExistsError:
        return []


# save tasks in json file
def save_tasks(tasks: dict):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)
        


task = Task(1, "Learn Python", "todo", "1990/90/20", "")

task_dict = {
    "id": 1,
    "description": "hello",
    "status": "done",
    "created_at": "1999",
    "updated_at": "2000"
}

task_list_done()
print("--------")
task_list_todo()
print("--------")
task_in_progress_tasks()