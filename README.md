# python-learning-journey
---

## Latest Progress (Refactored Architecture Update)

The project has now been upgraded from a single-file CLI script into a modular Python application.

### New System Structure

The codebase is now split into independent modules:

- `main.py` → Controls application flow (menu + startup)
- `tasks.py` → Handles task creation, storage, and display
- `mood.py` → Manages mood input and adaptive behavior system
- `user.py` → Handles user profile creation and loading
- `verses.py` → Generates random inspirational verses

---

### Key Improvements

- Modular architecture (each system has its own file)
- Reusable functions across the application
- Persistent data storage using JSON
- Mood-based adaptive UI behavior
- Dynamic inspirational verse on startup
- Cleaner separation of logic, storage, and interface

---

### Current Features (Working)

- User profile creation and loading
- Mood selection system with feedback messages
- Task management (add, view, mark as completed)
- Random verse display on startup
- Basic CLI navigation menu
- Persistent storage using JSON files

---

### 🚧 In Progress / Next Upgrades

- GUI version preview using Tkinter
- Button-based task management
- Improved mood analytics system
- Task editing and deletion features
- Better UI/UX structure for desktop app transition
