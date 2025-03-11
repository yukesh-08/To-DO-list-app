import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"✔ {task}")
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

complete_button = tk.Button(root, text="Mark Completed", command=mark_completed)
complete_button.pack()

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

load_tasks()

root.mainloop()