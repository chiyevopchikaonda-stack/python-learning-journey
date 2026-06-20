import random

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