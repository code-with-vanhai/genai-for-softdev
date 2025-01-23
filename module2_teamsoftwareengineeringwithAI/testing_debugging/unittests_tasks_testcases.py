import unittest
from tasks_testcases import TaskManager  # Assuming TaskManager is in tasks_testcases.py

class TestTaskManagerFunctional(unittest.TestCase):
    
    def setUp(self):
        """Set up a new instance of TaskManager before each test."""
        self.manager = TaskManager()

    def test_add_valid_task(self):
        """Test adding a valid task."""
        result = self.manager.add_task("Complete documentation")
        self.assertTrue(result)
        self.assertIn("Complete documentation", self.manager.list_tasks())

    def test_add_duplicate_task(self):
        """Test adding duplicate tasks."""
        self.manager.add_task("Review code")
        result = self.manager.add_task("Review code")
        self.assertFalse(result)  # Duplicate task should not be added

    def test_add_empty_task(self):
        """Test adding an empty task, should be rejected."""
        result = self.manager.add_task("")
        self.assertFalse(result)

    def test_add_whitespace_task(self):
        """Test adding a task with only spaces, should be rejected."""
        result = self.manager.add_task("     ")
        self.assertFalse(result)

    def test_remove_existing_task(self):
        """Test removing an existing task."""
        self.manager.add_task("Fix bugs")
        result = self.manager.remove_task("Fix bugs")
        self.assertTrue(result)
        self.assertNotIn("Fix bugs", self.manager.list_tasks())

    def test_remove_non_existing_task(self):
        """Test removing a task that doesn't exist."""
        result = self.manager.remove_task("Non-existing task")
        self.assertFalse(result)

    def test_list_tasks_when_empty(self):
        """Test listing tasks when no tasks are available."""
        result = self.manager.list_tasks()
        self.assertEqual(result, [])

    def test_list_tasks_with_multiple_entries(self):
        """Test listing tasks with multiple valid entries."""
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn("Task 1", tasks)
        self.assertIn("Task 2", tasks)

    def test_case_sensitivity_in_removal(self):
        """Test case sensitivity when removing tasks."""
        self.manager.add_task("Task 123")
        result = self.manager.remove_task("task 123")  # Different case
        self.assertFalse(result)
        self.assertIn("Task 123", self.manager.list_tasks())

    def test_remove_from_empty_list(self):
        """Test removing task from an empty list."""
        result = self.manager.remove_task("Some Task")
        self.assertFalse(result)

    def test_add_task_with_special_characters(self):
        """Test adding tasks with special characters."""
        result = self.manager.add_task("@#$%^&*()!")
        self.assertTrue(result)
        self.assertIn("@#$%^&*()!", self.manager.list_tasks())

    def test_add_long_task(self):
        """Test adding a very long task description."""
        long_task = "A" * 500
        result = self.manager.add_task(long_task)
        self.assertTrue(result)
        self.assertIn(long_task, self.manager.list_tasks())

    def test_remove_all_tasks(self):
        """Test removing all tasks and verifying the list is empty."""
        self.manager.add_task("Task A")
        self.manager.add_task("Task B")
        self.manager.remove_task("Task A")
        self.manager.remove_task("Task B")
        self.assertEqual(self.manager.list_tasks(), [])

if __name__ == '__main__':
    unittest.main()
