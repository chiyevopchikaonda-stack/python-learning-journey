import json
import os
MOOD_FILE="mood_history.json"
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

def set_mood(mood):
      save_mood(mood)
      return mood

def get_mood_insight():
      history = load_mood_history()
      if not history:
            return None
      return max(set(history), key=history.count)

def get_current_mood():
      history = load_mood_history()
      if not history:
            return None
      return history[-1]