import json
import os

TASK_FILE="tasks.json"

def load_tasks():
            if os.path.exists(TASK_FILE):
                with open(TASK_FILE,"r") as file:
                    return json.load(file)
                
            return []

def save_tasks(tasks):
            with open(TASK_FILE,"w") as file:
                json.dump(tasks,file)

def add_task():
            task_name=input("Enter task: ")
            due_date=input("Enter due date: ")

            task={
                "task": task_name,
                "due": due_date,
                "completed": False
            }

            tasks= load_tasks()
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!✔️")

def view_task(tasks):
            if not tasks:
                print("No tasks yet!📭")
                return
            
            print("\n 🗒️ Your Tasks:")

            for i, task in enumerate(tasks,1):
                status ="[✓]" if task.get("completed", False) else "[ ]"
                print(f"{i}. {status} {task['task']} - Due: {task['due']}")