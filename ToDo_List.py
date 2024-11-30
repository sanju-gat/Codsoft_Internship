# Task 1
# ToDo List


import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("My ToDo List")

        self.main_frame = tk.Frame(master)
        self.main_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.main_frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.main_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.label_task_entry = tk.Label(master, text="Type here:")
        self.label_task_entry.pack(pady=5)

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.pack(pady=5)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task:
            task_with_serial = f"{len(self.tasks) + 1}. {task}"
            self.task_listbox.insert(tk.END, task_with_serial)
            self.tasks.append(task_with_serial)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            if updated_task:
                task_with_serial = f"{selected_index + 1}. {updated_task}"
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, task_with_serial)
                self.tasks[selected_index] = task_with_serial
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to update.")
    
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index)
            self.renumber_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete.")

    def renumber_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            updated_task = f"{index + 1}. {task.split('. ', 1)[1]}"
            self.task_listbox.insert(tk.END, updated_task)
            self.tasks[index] = updated_task


ToDo = tk.Tk()
app = ToDoApp(ToDo)
ToDo.mainloop()
