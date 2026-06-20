import os
import json
import random
from tasks import load_tasks, save_tasks, add_task, view_task
from mood import get_mood, mood_behaviour, load_mood_history, save_mood, mood_insight
from user import load_or_create_user
from welcome import show_welcome

# Main menu
def main_menu(user,mood):
            while True:
                print("\n Anchor Study Main Menu")
                print(f"Current Mood: {mood}")
                behaviour=mood_behaviour.get(mood,mood_behaviour["Okay"])
                print(behaviour["message"])
                print("1. View Profile")
                print("2. Add Task")
                print("3. View Tasks")
                print("4. Complete Task")
                print("5. Exit")

                choice = input("Select an option: ")

                if choice == "1":
                    print("\n 👤 Profile")
                    print("Name:", user["name"])
                    print("Education:", user["education"])

                elif choice == "2":
                    add_task()
                    
                elif choice == "3":
                    tasks = load_tasks()

                    if not tasks:
                        print("No tasks yet!📭")
                        continue

                    behaviour = mood_behaviour.get(mood, mood_behaviour["Okay"])
                    mode = behaviour["task_mode"]

                    if mode == "minimal":
                          view_task(tasks[:1])

                    elif mode == "light":
                          view_task(tasks[:3])
                    else :
                        view_task(tasks)

                elif choice == "4":
                    tasks = load_tasks()

                    if not tasks:
                            print("No tasks to complete!📭")
                            continue
                    
                    print("\n 🗒️ Your Tasks:")
                    for i, task in enumerate(tasks,1):
                        status ="[✓]" if task.get("completed", False) else "[ ]"
                        print(f"{i}. {status} {task['task']} - Due: {task['due']}")

                        try:
                              task_num=int(input("\nEnter task number to mark as completed: ")) - 1

                              if 0 <= task_num < len(tasks):
                                tasks[task_num]["completed"] = True
                                save_tasks(tasks)
                                print("Task marked as completed!✔️")
                              else:
                                print("Invalid task number!❌")
                        except ValueError:
                              print("Please enter a valid number!❌")

                elif choice == "5":
                        print("Goodbye!👋")
                        break
                else:
                    print("Invalid option, please try again.❌")
            
# start program

show_welcome()
mood=get_mood()
mood_insight()
user = load_or_create_user()
print("\nYour personal study assistant is here to help you stay organized and focused on your studies!📚")
main_menu(user,mood)




                  
