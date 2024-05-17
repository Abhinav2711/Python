import tkinter as tk
from tkinter import messagebox
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the listbox and scrollbar
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(
            frame,
            width=50,
            height=10,
            selectmode=tk.SINGLE
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Entry widget to add new tasks
        self.task_entry = tk.Entry(
            self.root,
            width=50
        )
        self.task_entry.pack(pady=10)

        # Buttons to add, edit, and delete tasks
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        add_task_btn = tk.Button(
            btn_frame,
            text="Add Task",
            command=self.add_task
        )
        add_task_btn.pack(side=tk.LEFT, padx=5)

        edit_task_btn = tk.Button(
            btn_frame,
            text="Edit Task",
            command=self.edit_task
        )
        edit_task_btn.pack(side=tk.LEFT, padx=5)

        delete_task_btn = tk.Button(
            btn_frame,
            text="Delete Task",
            command=self.delete_task
        )
        delete_task_btn.pack(side=tk.LEFT, padx=5)

        mark_completed_btn = tk.Button(
            btn_frame,
            text="Mark Completed",
            command=self.mark_completed
        )
        mark_completed_btn.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = self.tasks[selected_task_index[0]]
            new_task = self.task_entry.get()
            if new_task != "":
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task description.")
        else:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            completed_task = self.tasks[selected_task_index[0]] + " (Completed)"
            self.tasks[selected_task_index[0]] = completed_task
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()