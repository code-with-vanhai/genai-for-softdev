import threading

class TaskManager:
    def __init__(self):
        """Initialize an empty task list with a lock for thread safety."""
        self.tasks = []
        self.lock = threading.Lock()

    def add_task(self, task):
        """Add a new task to the list with thread safety."""
        task = task.strip()  # Remove leading and trailing whitespace
        if not task:
            print("Error: Task cannot be empty or only whitespace.")
            return False

        with self.lock:
            if task in self.tasks:
                print(f"Error: Task '{task}' already exists.")
                return False
            self.tasks.append(task)
            print(f'Task "{task}" added successfully.')
            return True

    def remove_task(self, task):
        """Remove a task from the list with thread safety."""
        with self.lock:
            if not self.tasks:
                print("Error: No tasks available to remove.")
                return False
            if task in self.tasks:
                self.tasks.remove(task)
                print(f'Task "{task}" removed successfully.')
                return True
            else:
                print(f'Error: Task "{task}" not found.')
                return False

    def list_tasks(self):
        """List all tasks with thread safety."""
        with self.lock:
            if not self.tasks:
                print("No tasks available.")
                return []
            print("Current Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
            return list(self.tasks)  # Return a copy to avoid concurrency issues

# Test cases to verify thread safety
if __name__ == "__main__":
    import concurrent.futures

    manager = TaskManager()

    def add_tasks():
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")

    def remove_tasks():
        manager.remove_task("Task 1")
        manager.remove_task("Task 2")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(add_tasks)
        executor.submit(remove_tasks)
        executor.submit(manager.list_tasks)
