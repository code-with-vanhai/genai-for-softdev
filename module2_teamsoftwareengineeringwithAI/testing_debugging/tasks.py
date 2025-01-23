class TaskManager:
    def __init__(self):
        """Initialize an empty task list."""
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        if task:
            self.tasks.append(task)
            print(f'Task "{task}" added successfully.')
        else:
            print("Task cannot be empty.")

    def remove_task(self, task):
        """Remove a task from the list."""
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed successfully.')
        else:
            print(f'Task "{task}" not found in the list.')

    def list_tasks(self):
        """List all tasks."""
        if self.tasks:
            print("Current Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("No tasks available.")

# Example usage
if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Complete project documentation")
    manager.add_task("Review pull requests")
    manager.add_task("Prepare for team meeting")

    manager.list_tasks()

    manager.remove_task("Review pull requests")

    manager.list_tasks()
