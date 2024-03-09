import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    if task:
        tasks.insert(tk.END, (task, priority))
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = tasks.curselection()[0]
        tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
    if confirmed:
        tasks.delete(0, tk.END)

def mark_as_completed():
    try:
        task_index = tasks.curselection()[0]
        task = tasks.get(task_index)
        task_text, priority = task[0], task[1]
        tasks.delete(task_index)
        completed_tasks.insert(tk.END, (task_text, priority))
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

root = tk.Tk()
root.title("Interactive To-Do List App")
root.configure(background="#f0f0f0")

task_entry = tk.Entry(root, width=40, bg="#FFFFFF")
task_entry.pack(pady=10)

priority_var = tk.StringVar(root)
priority_var.set("Low")

priority_frame = tk.Frame(root, background="#f0f0f0")
priority_frame.pack()

priority_label = tk.Label(priority_frame, text="Priority:", background="#f0f0f0")
priority_label.pack(side=tk.LEFT, padx=(10, 5))

priority_menu = tk.OptionMenu(priority_frame, priority_var, "Low", "Medium", "High")
priority_menu.pack(side=tk.LEFT)

add_button = tk.Button(root, text="Add Task", command=add_task, background="#4CAF50", fg="white", padx=10, pady=5)
add_button.pack(pady=(10, 0))

delete_button = tk.Button(root, text="Delete Task", command=delete_task, background="#FF5733", fg="white", padx=10, pady=5)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, background="#4286f4", fg="white", padx=10, pady=5)
clear_button.pack(pady=5)

mark_as_completed_button = tk.Button(root, text="Mark as Completed", command=mark_as_completed, background="#4CAF50", fg="white", padx=10, pady=5)
mark_as_completed_button.pack(pady=5)

tasks_frame = tk.Frame(root, background="#f0f0f0")
tasks_frame.pack(padx=10, pady=10)

tasks_label = tk.Label(tasks_frame, text="To-Do:", background="#f0f0f0")
tasks_label.grid(row=0, column=0)

tasks = tk.Listbox(tasks_frame, width=40, bg="#FFFFFF")
tasks.grid(row=1, column=0)

completed_tasks_label = tk.Label(tasks_frame, text="Completed:", background="#f0f0f0")
completed_tasks_label.grid(row=0, column=1)

completed_tasks = tk.Listbox(tasks_frame, width=40, bg="#FFFFFF")
completed_tasks.grid(row=1, column=1)

root.mainloop()
