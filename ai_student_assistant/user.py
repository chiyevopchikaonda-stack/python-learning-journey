import json
import os
USER_FILE ="user.json"

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

def load_user():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return json.load(file)
    return None

def save_user(user):
    with open(USER_FILE, "w") as file:
        json.dump(user, file)
