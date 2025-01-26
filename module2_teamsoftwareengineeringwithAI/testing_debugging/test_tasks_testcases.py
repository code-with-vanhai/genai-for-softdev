import pytest
from threading import Thread
from tasks_testcases import TaskManager  # Assuming the code is in tasks_testcases.py

def test_add_task():
    tm = TaskManager()
    assert tm.add_task("Task 1") == True
    assert tm.add_task("Task 1") == False  # Duplicate task
    assert tm.add_task("  ") == False  # Empty task
    assert tm.add_task("Task 2") == True

def test_remove_task():
    tm = TaskManager()
    tm.add_task("Task 1")
    assert tm.remove_task("Task 1") == True  # Successful removal
    assert tm.remove_task("Task 1") == False  # Task not found
    assert tm.remove_task("Task 2") == False  # Non-existent task

def test_list_tasks():
    tm = TaskManager()
    assert tm.list_tasks() == []  # Empty list
    tm.add_task("Task 1")
    tm.add_task("Task 2")
    assert tm.list_tasks() == ["Task 1", "Task 2"]

def test_concurrent_access():
    tm = TaskManager()
    
    def add_tasks():
        for _ in range(100):
            tm.add_task("Task")
    
    def remove_tasks():
        for _ in range(100):
            tm.remove_task("Task")
    
    thread1 = Thread(target=add_tasks)
    thread2 = Thread(target=remove_tasks)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    assert tm.list_tasks() == [] or tm.list_tasks() == ["Task"]

def test_whitespace_handling():
    tm = TaskManager()
    assert tm.add_task("  Task  ") == True  # Trimmed task should be added
    assert tm.add_task("Task") == False  # Duplicate check should pass with trimmed version

def test_remove_from_empty_list():
    tm = TaskManager()
    assert tm.remove_task("Task") == False  # No tasks to remove

def test_edge_cases():
    tm = TaskManager()
    assert tm.add_task("") == False  # Empty string
    assert tm.add_task("  ") == False  # Only spaces
    assert tm.add_task("\n") == False  # Only newline
    assert tm.add_task("Task") == True
    assert tm.add_task("Task") == False  # Adding same task again
    assert tm.remove_task("NonExistent") == False  # Removing non-existent task
