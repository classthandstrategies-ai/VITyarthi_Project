import json
import os
from datetime import datetime

DATA_FILE = "my_tasks.json"


class Task:
    """
    Represents a single academic task.
    """

    def __init__(self, task_id, title, subject, due_date, priority, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.subject = subject
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def to_dict(self):
        """Converts task object to dictionary for JSON saving."""
        return {
            "id": self.task_id,
            "title": self.title,
            "subject": self.subject,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        """Creates a Task object from a dictionary."""
        return Task(data['id'], data['title'], data['subject'], data['due_date'], data['priority'], data['status'])


class TaskManager:
    """
    Handles all CRUD operations and logic.
    """

    def __init__(self):
        self.tasks = []
        self.load_data()

    def load_data(self):
        """Reads data from the JSON file (File Handling)."""
        if not os.path.exists(DATA_FILE):
            return

        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(t) for t in data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"[Error] Could not load data: {e}")

    def save_data(self):
        """Saves current list to JSON file (Persistence)."""
        try:
            with open(DATA_FILE, 'w') as f:
                json.dump([t.to_dict() for t in self.tasks], f, indent=4)
            print("\n[Success] Data saved successfully.")
        except IOError as e:
            print(f"[Error] Could not save data: {e}")

    def add_task(self, title, subject, due_date, priority):

        new_id = 1 if not self.tasks else max(t.task_id for t in self.tasks) + 1
        new_task = Task(new_id, title, subject, due_date, priority)
        self.tasks.append(new_task)
        self.save_data()
        print(f"\n[Success] Task '{title}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("\n[Info] No tasks found.")
            return

        print("\n--- Your Academic Tasks ---")
        print(f"{'ID':<5} {'Title':<20} {'Subject':<15} {'Priority':<10} {'Status':<10} {'Due Date'}")
        print("-" * 75)
        for t in self.tasks:
            print(
                f"{t.task_id:<5} {t.title[:18]:<20} {t.subject[:13]:<15} {t.priority:<10} {t.status:<10} {t.due_date}")

    def mark_completed(self, task_id):
        for t in self.tasks:
            if t.task_id == task_id:
                t.status = "Completed"
                self.save_data()
                print(f"\n[Success] Task ID {task_id} marked as Completed.")
                return
        print("\n[Error] Task ID not found.")

    def delete_task(self, task_id):
        original_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.task_id != task_id]

        if len(self.tasks) < original_count:
            self.save_data()
            print(f"\n[Success] Task ID {task_id} deleted.")
        else:
            print("\n[Error] Task ID not found.")

    def get_statistics(self):
        """Analytical function to show progress."""
        total = len(self.tasks)
        if total == 0:
            return "No tasks available to analyze."

        completed = sum(1 for t in self.tasks if t.status == "Completed")
        pending = total - completed
        return f"Total: {total} | Completed: {completed} | Pending: {pending}"


def input_validation(prompt, valid_options=None):
    """Helper for input validation/error handling."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("[Error] Input cannot be empty.")
            continue
        if valid_options and value not in valid_options:
            print(f"[Error] Please choose from {valid_options}")
            continue
        return value


def main():
    manager = TaskManager()

    while True:
        print("\n=== VITyarthi Academic Planner ===")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. View Statistics")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            title = input_validation("Enter Task Title: ")
            subject = input_validation("Enter Subject Name: ")
            date = input_validation("Enter Due Date (DD-MM-YYYY): ")
            prio = input_validation("Enter Priority (High/Medium/Low): ", ["High", "Medium", "Low"])
            manager.add_task(title, subject, date, prio)

        elif choice == '2':
            manager.view_tasks()

        elif choice == '3':
            try:
                t_id = int(input("Enter Task ID to mark complete: "))
                manager.mark_completed(t_id)
            except ValueError:
                print("[Error] Please enter a valid numeric ID.")

        elif choice == '4':
            try:
                t_id = int(input("Enter Task ID to delete: "))
                manager.delete_task(t_id)
            except ValueError:
                print("[Error] Please enter a valid numeric ID.")

        elif choice == '5':
            print(f"\n[Analytics] {manager.get_statistics()}")

        elif choice == '6':
            print("Exiting VITyarthi Planner. Good luck with your studies!")
            break
        else:
            print("[Error] Invalid selection.")


if __name__ == "__main__":
    main()