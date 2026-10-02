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
    

# create task 
def add(description):
    tasks = load_tasks()
    current_time = datetime.now()
    
    new_task = Task(
        1,
        description,
        "todo",
        current_time.strftime("%Y/%m/%d - %H:%M"),
        "-"
    )
    
    task_dict = asdict(new_task)
    
    tasks.append(task_dict)
    
    save_tasks(tasks)


# update task
def update(task_id, description):
    tasks = load_tasks()
    current_time = datetime.now()
    
    for i in tasks:
        if i["id"] == task_id:
            task = i
    
    task["description"] = description
    task["updated_at"] = current_time.strftime("%Y/%m/%d - %H:%M")
    
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


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("description", type=str)
    
    # update
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("description", type=str)
    
    # make task in progress
    mark_in_progress_parser = subparsers.add_parser("mark-in-progress")
    mark_in_progress_parser.add_argument("id", type=int)
    
    # make task done
    mark_done_parser = subparsers.add_parser("mark-done")
    mark_done_parser.add_argument("id", type=int)
    
    # list
    list_parser = subparsers.add_parser("list")
    
    # # listing task by status
    # list_parser.add_subparsers(dest="list-commands")
    # list_parser.subparsers.add_parser("list-todo")
    # list_parser.subparsers.add_parser("list-in-progress")
    
    args = parser.parse_args()

    if args.command == "add":
        add(args.description)
        
    if args.command == "update":
        update(args.id, args.description)

    if args.command == "delete":
        delete(args.id)
    
    if args.command == "mark-in-progress":
        mark_in_progress(args.id)
        
    if args.command == "mark-done":
        mark_done(args.id)

    if args.command == "list":
        task_list()



    print(args)


if __name__ == "__main__":
    main()