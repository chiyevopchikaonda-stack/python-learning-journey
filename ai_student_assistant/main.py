import os
import json
import random

# files for storing user data and tasks
USER_FILE="user.json"
TASK_FILE="tasks.json"
MOOD_FILE="mood.json"

verses = [
    {
        "text": "I can do all things through Christ who strengthens me.",
        "reference": "Philippians 4:13"
    },
    {
        "text": "Be strong and courageous. Do not be afraid.",
        "reference": "Joshua 1:9"
    },
    {
        "text": "The Lord is my shepherd; I shall not want.",
        "reference": "Psalm 23:1"
    },
     {
        "text": "For God did not give us a spirit of fear, but of power, and of love, and of a sound mind;",
        "reference": "2 Timothy 1:7"
    }
]

# Welcome page

def show_welcome():
      verse= random.choice(verses)
      print("\nWelcome to Anchor Study!⚓")
      print("-------------------------------------")
      print("\nWord of the Day:")
      print(verse["text"])
      print(f"- {verse['reference']}\n")
      print("--------------------------------------\n")


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

            # Mood system

moods = {
    "1": "Motivated",
    "2": "Okay",
    "3": "Tired",
    "4": "Stressed"
}
def get_mood():
      print("\nHow are you feeling today?")
      print("1. 😄 Motivated")
      print("2. 🙂 Okay")
      print("3. 😴 Tired")
      print("4. 😰 Stressed")
      choice= input("\nSelect (1-4): ")
      mood = moods.get(choice,"Okay")
      print(f"Your mood is: {mood}")
      save_mood(mood)
      return mood

mood_behaviour={
      "Motivated": {
            "message": "Let's keep that energy going!💪",
            "task_mode": "heavy"
      },
      "Okay": {
            "message": "Steady progress is still progress. Keep going!🚀",
            "task_mode": "normal"
      },
      "Tired": {
            "message": "Remember to take breaks and rest when needed.😴",
            "task_mode": "light"
      },
      "Stressed": {
            "message": "Breathe and take it one step at a time. You've got this!🌟",
            "task_mode": "minimal"
      }
}
def load_mood_history():
      if os.path.exists(MOOD_FILE):
            with open(MOOD_FILE,"r") as file:
                return json.load(file)
      return []
def save_mood(mood):
      history = load_mood_history()
      history.append(mood)
      with open(MOOD_FILE,"w") as file:
            json.dump(history,file)  
def mood_insight():
      history = load_mood_history()
      if not history:             
        print("No mood history yet!📭")
        return 
      most_common = max(set(history), key=history.count)
      print("\nMood Insights📊:")
      print(f"You've mostly been feeling: {most_common}")

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

def main_menu(user,mood):
            while True:
                print("\n Anchor Study Main Menu")
                print(f"Current Mood: {mood}")
                behaviour=mood_behaviour.get(mood,mood_behaviour["Okay"])
                print(behaviour["message"])
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
                    tasks = load_tasks()
                    if not tasks:
                        print("No tasks yet!📭")
                        continue
                    behaviour = mood_behaviour.get(mood, mood_behaviour["Okay"])
                    mode = behaviour["task_mode"]
                    if mode == "minimal":
                          print("\nFocus Mode (only 1 task)")
                          for i, task in enumerate(tasks[:1], 1):
                                print(f"{i}. {task['task']} - Due: {task['due']}")
                    elif mode == "light":
                          print("\nLight Mode (up to 3 tasks)")
                          for i, task in enumerate(tasks[:3], 1):
                                print(f"{i}. {task['task']} - Due: {task['due']}")
                    else :
                        view_task()
                elif choice == "4":
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




                  
