"""
Todo Console Application - User Interface

This module provides the command-line interface for the todo application.
"""
from typing import Optional
from service import TaskService
from storage import TaskStorage
from models import Task


class TodoCLI:
    """
    Command-line interface for the todo application.

    Provides menu-driven interface with clear prompts and feedback,
    handling input validation and error messages while maintaining
    separation from business logic and storage concerns.
    """

    def __init__(self, service=None, storage=None):
        """
        Initialize the CLI with storage and service instances.

        Args:
            service: TaskService instance (optional, creates new if None)
            storage: TaskStorage instance (optional, creates new if None)
        """
        if storage is None:
            self.storage = TaskStorage()
        else:
            self.storage = storage

        if service is None:
            self.service = TaskService(self.storage)
        else:
            self.service = service

    def display_menu(self) -> None:
        """Display the main menu options."""
        print("\n=== Todo App Menu ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Complete")
        print("6. Exit")

    def get_choice(self) -> int:
        """
        Get the user's menu choice with validation.

        Returns:
            int: The user's choice (1-6)
        """
        while True:
            try:
                choice = int(input("\nEnter choice (1-6): ").strip())
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Invalid option. Please enter a number between 1-6")
            except ValueError:
                print("Invalid option. Please enter a number between 1-6")

    def view_tasks_flow(self) -> None:
        """Display all tasks in table format with summary information."""
        tasks = self.service.list_tasks()
        if not tasks:
            print("\nNo tasks found.")
            return

        print("\nID | Title           | Status    | Created")
        print("-" * 50)
        for task in tasks:
            status = "✓ Complete" if task.completed else "☐ Pending"
            created_str = task.created_at.strftime("%Y-%m-%d %H:%M")
            title = task.title[:13] + "..." if len(task.title) > 13 else task.title
            print(f"{task.id:<2} | {title:<13} | {status:<9} | {created_str}")

        # Show summary
        total = len(tasks)
        completed = sum(1 for task in tasks if task.completed)
        pending = total - completed
        print(f"\n[INFO] You have {total} tasks "
              f"({pending} pending, {completed} completed)")

    def add_task_flow(self) -> None:
        """Add a new task with validation."""
        title = input("\nEnter task title: ").strip()
        if not title:
            print("[WARNING] Title cannot be empty")
            return

        description = input("Enter task description (optional): ").strip()
        success, message, task = self.service.create_task(title, description)
        print(message)

    def update_task_flow(self) -> None:
        """Update an existing task."""
        try:
            task_id = int(input("\nEnter task ID to update: "))
            tasks = self.service.list_tasks()
            task = next((t for t in tasks if t.id == task_id), None)
            if not task:
                print(f"[ERROR]: Task not found with ID: {task_id}. Use option 2 to view all tasks")
                return

            print(f"Current task: {task}")
            new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
            new_description = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()

            # Use current values if user didn't provide new ones
            title = new_title if new_title else None
            description = new_description if new_description else None

            success, message = self.service.update_task(task_id, title=title, description=description)
            print(message)
        except ValueError:
            print("[ERROR]: Please enter a valid task ID (number)")

    def delete_task_flow(self) -> None:
        """Delete a task with confirmation."""
        try:
            task_id = int(input("\nEnter task ID to delete: "))
            tasks = self.service.list_tasks()
            task = next((t for t in tasks if t.id == task_id), None)
            if not task:
                print(f"[ERROR]: Task not found with ID: {task_id}. Use option 2 to view all tasks")
                return

            confirm = input(f"Are you sure you want to delete task '{task.title}'? (y/n): ").strip().lower()
            if confirm in ['y', 'yes']:
                success, message = self.service.delete_task(task_id)
                print(message)
            else:
                print("Deletion cancelled.")
        except ValueError:
            print("[ERROR]: Please enter a valid task ID (number)")

    def toggle_complete_flow(self) -> None:
        """Toggle a task's completion status."""
        try:
            task_id = int(input("\nEnter task ID to toggle: "))
            tasks = self.service.list_tasks()
            task = next((t for t in tasks if t.id == task_id), None)
            if not task:
                print(f"[ERROR]: Task not found with ID: {task_id}. Use option 2 to view all tasks")
                return

            success, message = self.service.toggle_complete(task_id)
            print(message)
        except ValueError:
            print("[ERROR]: Please enter a valid task ID (number)")

    def run(self) -> None:
        """Run the main application loop."""
        print("Welcome to the Todo Console Application!")

        while True:
            self.display_menu()
            choice = self.get_choice()

            if choice == 1:
                self.add_task_flow()
            elif choice == 2:
                self.view_tasks_flow()
            elif choice == 3:
                self.update_task_flow()
            elif choice == 4:
                self.delete_task_flow()
            elif choice == 5:
                self.toggle_complete_flow()
            elif choice == 6:
                print("\nThank you for using the Todo Console Application!")
                break