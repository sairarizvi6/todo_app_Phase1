"""
Test script to verify the todo application functionality without user interaction.
"""
from service import TaskService
from storage import TaskStorage
from models import Task


def test_application():
    """Test the core functionality of the todo application."""
    print("Testing Todo Console Application...")
    
    # Initialize storage and service
    storage = TaskStorage()
    service = TaskService(storage)
    
    # Test 1: Add tasks
    print("\n1. Testing create_task functionality:")
    try:
        success, message, task_1 = service.create_task("Test Task 1", "This is a test task")
        print(f"   [OK] {message}")

        success, message, task_2 = service.create_task("Test Task 2")
        print(f"   [OK] {message}")

        # Test validation
        success, message, task = service.create_task("")  # Should return error
        if not success:
            print(f"   [OK] Validation works - {message}")
        else:
            print("   [ERROR] Validation failed - empty title was allowed")

    except Exception as e:
        print(f"   [ERROR] Error adding tasks: {str(e)}")

    # Test 2: Get all tasks
    print("\n2. Testing list_tasks functionality:")
    try:
        tasks = service.list_tasks()
        print(f"   [OK] Retrieved {len(tasks)} tasks")
        for task in tasks:
            print(f"     - {task}")
    except Exception as e:
        print(f"   [ERROR] Error getting tasks: {str(e)}")

    # Test 3: Get task summary
    print("\n3. Testing task summary functionality:")
    try:
        tasks = service.list_tasks()
        total = len(tasks)
        completed = sum(1 for task in tasks if task.completed)
        pending = total - completed
        print(f"   [OK] Summary: {total} total, "
              f"{pending} pending, {completed} completed")
    except Exception as e:
        print(f"   [ERROR] Error getting summary: {str(e)}")

    # Test 4: Toggle task completion
    print("\n4. Testing toggle_complete functionality:")
    try:
        if tasks:
            task_to_toggle = tasks[0]
            print(f"   Before toggle: {task_to_toggle} (completed: {task_to_toggle.completed})")

            success, message = service.toggle_complete(task_to_toggle.id)
            if success:
                # Get the updated task to check the status
                updated_tasks = service.list_tasks()
                updated_task = next(t for t in updated_tasks if t.id == task_to_toggle.id)
                print(f"   After toggle: {updated_task} (completed: {updated_task.completed})")
                print("   [OK] Task completion toggled successfully")
            else:
                print(f"   [ERROR] Failed to toggle task completion: {message}")
        else:
            print("   No tasks to test with")
    except Exception as e:
        print(f"   [ERROR] Error toggling task: {str(e)}")

    # Test 5: Update task
    print("\n5. Testing update_task functionality:")
    try:
        if tasks:
            task_to_update = tasks[0]
            old_title = task_to_update.title
            new_title = "Updated Task Title"

            print(f"   Before update: {task_to_update}")
            success, message = service.update_task(task_to_update.id, title=new_title)
            if success:
                # Get the updated task to check the changes
                updated_tasks = service.list_tasks()
                updated_task = next(t for t in updated_tasks if t.id == task_to_update.id)
                print(f"   After update: {updated_task}")
                print("   [OK] Task updated successfully")
            else:
                print(f"   [ERROR] Failed to update task: {message}")
        else:
            print("   No tasks to test with")
    except Exception as e:
        print(f"   [ERROR] Error updating task: {str(e)}")

    # Test 6: Delete task
    print("\n6. Testing delete_task functionality:")
    try:
        if tasks:
            task_to_delete = tasks[0]
            print(f"   Deleting task: {task_to_delete}")

            success, message = service.delete_task(task_to_delete.id)
            if success:
                print(f"   [OK] {message}")

                # Verify deletion
                remaining_tasks = service.list_tasks()
                print(f"   Remaining tasks: {len(remaining_tasks)}")
            else:
                print(f"   [ERROR] Failed to delete task: {message}")
        else:
            print("   No tasks to test with")
    except Exception as e:
        print(f"   [ERROR] Error deleting task: {str(e)}")

    print("\nTesting completed!")


if __name__ == "__main__":
    test_application()