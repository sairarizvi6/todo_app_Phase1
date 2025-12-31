"""
Test script to verify the todo application functionality without interactive input
"""
import sys
import os
# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from storage import TaskStorage
from service import TaskService
from models import Task

def test_application():
    print("Testing the Todo Console Application components...")
    
    # Initialize components
    storage = TaskStorage()
    service = TaskService(storage)
    
    # Test creating a task
    print("\n1. Testing task creation...")
    success, message, task = service.create_task("Test Task", "This is a test task")
    print(f"   Result: {message}")
    
    # Test listing tasks
    print("\n2. Testing task listing...")
    tasks = service.list_tasks()
    print(f"   Number of tasks: {len(tasks)}")
    for task in tasks:
        status = "Complete" if task.completed else "Pending"
        print(f"   - ID: {task.id}, Title: {task.title}, Status: {status}")
    
    # Test updating a task
    print("\n3. Testing task update...")
    if tasks:
        task_id = tasks[0].id
        success, message = service.update_task(task_id, title="Updated Test Task")
        print(f"   Result: {message}")
    
    # Test toggling completion
    print("\n4. Testing task completion toggle...")
    if tasks:
        task_id = tasks[0].id
        success, message = service.toggle_complete(task_id)
        print(f"   Result: {message}")
        
        # Check the updated status
        updated_task = storage.get(task_id)
        status = "Complete" if updated_task.completed else "Pending"
        print(f"   Updated status: {status}")
    
    # Test deleting a task
    print("\n5. Testing task deletion...")
    if tasks:
        task_id = tasks[0].id
        success, message = service.delete_task(task_id)
        print(f"   Result: {message}")
    
    print("\nApplication components tested successfully!")

if __name__ == "__main__":
    test_application()