"""
Demo script showing the Todo CLI application functionality
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from storage import TaskStorage
from service import TaskService
from cli import TodoCLI

def demo_application():
    print("Todo CLI Application Demo")
    print("="*30)

    # Initialize the application components
    storage = TaskStorage()
    service = TaskService(storage)
    cli = TodoCLI(service=service, storage=storage)

    print("\n1. Adding a new task:")
    print("   User selects option 1 (Add Task)")
    print("   User enters 'Buy groceries' as title")
    print("   User enters 'Milk, bread, eggs' as description")

    # Simulate adding a task
    success, message, task = service.create_task("Buy groceries", "Milk, bread, eggs")
    print(f"   -> {message}")

    print("\n2. Adding another task:")
    success, message, task2 = service.create_task("Finish report", "Complete the quarterly report for work")
    print(f"   -> {message}")

    print("\n3. Viewing all tasks:")
    print("   User selects option 2 (View All Tasks)")
    print("   Application displays:")

    # Show how tasks would be displayed
    tasks = service.list_tasks()
    print("   \nID | Title           | Status    | Created")
    print("   " + "-" * 50)
    for task in tasks:
        status = "Complete" if task.completed else "Pending"
        created_str = task.created_at.strftime("%Y-%m-%d %H:%M")
        title = task.title[:13] + "..." if len(task.title) > 13 else task.title
        print(f"   {task.id:<2} | {title:<13} | {status:<9} | {created_str}")

    # Show summary
    total = len(tasks)
    completed = sum(1 for task in tasks if task.completed)
    pending = total - completed
    print(f"   \n   [INFO] You have {total} tasks ({pending} pending, {completed} completed)")

    print("\n4. Updating a task:")
    print("   User selects option 3 (Update Task)")
    print("   User enters task ID 1")
    print("   User enters new title 'Buy groceries for dinner'")
    success, message = service.update_task(1, title="Buy groceries for dinner")
    print(f"   -> {message}")

    print("\n5. Toggling task completion:")
    print("   User selects option 5 (Toggle Complete)")
    print("   User enters task ID 1")
    success, message = service.toggle_complete(1)
    print(f"   -> {message}")

    print("\n6. Deleting a task:")
    print("   User selects option 4 (Delete Task)")
    print("   User enters task ID 2")
    print("   Application asks for confirmation")
    print("   User confirms deletion")
    success, message = service.delete_task(2)
    print(f"   -> {message}")

    print("\n7. Viewing remaining tasks:")
    print("   User selects option 2 (View All Tasks)")
    remaining_tasks = service.list_tasks()
    print("   \nID | Title                    | Status    | Created")
    print("   " + "-" * 55)
    for task in remaining_tasks:
        status = "Complete" if task.completed else "Pending"
        created_str = task.created_at.strftime("%Y-%m-%d %H:%M")
        title = task.title[:20] + "..." if len(task.title) > 20 else task.title
        print(f"   {task.id:<2} | {title:<20} | {status:<9} | {created_str}")

    print(f"\n   [INFO] You have {len(remaining_tasks)} tasks remaining")

    print("\n8. Exiting application:")
    print("   User selects option 6 (Exit)")
    print("   Application exits gracefully")

    print("\n" + "="*30)
    print("Demo completed! The Todo CLI application is fully functional.")
    print("\nTo run the actual application, use:")
    print("   cd todo-console-app/src && python main.py")
    print("\nNote: The application requires an interactive terminal that supports user input.")

if __name__ == "__main__":
    demo_application()