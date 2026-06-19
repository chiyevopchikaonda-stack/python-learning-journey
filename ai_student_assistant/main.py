import os
import json

# files for storing user data and tasks
USER_FILE="user.json"
TASK_FILE="tasks.json"

# User system

def load_or_create_user():
    if os.path.exists(USER_FILE):
            with open(USER_FILE,"r") as file:
                user=json.load(file)
                print(f"Welcome back, {user['name']}!😊")
                return user
    else:
            print("Let's create your profile!📝")
            name= input("What is your name? ")
            education = input("What is your education level? ")
            user={
                "name": name,
                "education": education
            }
            with open(USER_FILE,"w") as file:
                json.dump(user,file)
                print("Profile created successfully!")
                return user 
            user = load_or_create_user()

            # Task system

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
                "due": due_date
            }
            tasks= load_tasks()
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!✅")
def view_task():
            tasks= load_tasks()
            if not tasks:
                print("No tasks yet!📭")
                return
            print("\n 🗒️ Your Tasks:")
            for i, task in enumerate(tasks,1):
                print(f"{i}. {task['task']} - Due: {task['due']}")

            # Main menu

def main_menu(user):
            while True:
                print("\n Anchor Study Main Menu")
                print("1. View Profile")
                print("2. Add Task")
                print("3. View Tasks")
                print("4. Exit")
                choice = input("Select an option: ")
                if choice == "1":
                    print("\n 👤 Profile")
                    print("Name:", user["name"])
                    print("Education:", user["education"])
                elif choice == "2":
                    add_task()
                elif choice == "3":
                    view_task()
                elif choice == "4":
                        print("Goodbye!👋")
                        break
                else:
                    print("Invalid option, please try again.❌")

# start program

user = load_or_create_user()
main_menu(user)



                  
