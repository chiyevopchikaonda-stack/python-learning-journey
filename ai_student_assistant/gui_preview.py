import tkinter as tk
from tkinter import messagebox
import re
from tasks import load_tasks, save_tasks


def is_valid_date(date_text):
    return re.match(r"^\d{2}/\d{2}/\d{4}$", date_text)


root = tk.Tk()
root.title("Anchor Study")

header = tk.Frame(root)
header.pack()

tk.Label(header, text="⚓ Anchor Study ⚓").pack()
tk.Label(header, text="Welcome back, Chiyevo!").pack()

mood_frame = tk.Frame(root)
mood_frame.pack()

tk.Label(mood_frame, text="Mood: 🙂 Okay").pack()

task_frame = tk.Frame(root)
task_frame.pack()


def refresh_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    tk.Label(task_frame, text="Your Tasks:").pack()

    tasks = load_tasks()

    for task in tasks:
        status = "✔️" if task.get("completed", False) else "[ ]"
        tk.Label(
            task_frame,
            text=f"{status} {task['task']} - Due: {task['due']}"
        ).pack()


refresh_tasks()


def open_add_task():
    popup = tk.Toplevel(root)
    popup.title("Add Task")

    tk.Label(popup, text="Task Name").pack()
    task_entry = tk.Entry(popup)
    task_entry.pack()

    tk.Label(popup, text="Due Date (dd/mm/yyyy)").pack()
    due_entry = tk.Entry(popup)
    due_entry.pack()

    def save_task():
        task = task_entry.get()
        due = due_entry.get()

        if not task.strip():
            messagebox.showerror(
                "Missing Task",
                "Please enter a task name."
            )
            return

        if not due.strip():
            messagebox.showerror(
                "Missing Date",
                "Please enter a due date."
            )
            return

        if not is_valid_date(due):
            messagebox.showerror(
                "Invalid Date",
                "Please use the format dd/mm/yyyy."
            )
            return

        tasks = load_tasks()

        tasks.append({
            "task": task,
            "due": due,
            "completed": False
        })

        save_tasks(tasks)
        refresh_tasks()

        messagebox.showinfo(
            "Success",
            "Task added successfully!"
        )

        popup.destroy()

    tk.Button(
        popup,
        text="Save Task",
        command=save_task
    ).pack()


tk.Button(
    root,
    text="Add Task",
    command=open_add_task
).pack()

root.mainloop()