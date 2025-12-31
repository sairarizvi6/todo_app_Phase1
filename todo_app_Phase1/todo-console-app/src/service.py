"""
Todo Console Application - Business Logic

This module contains the business logic for the todo application.
"""
from typing import List, Optional, Tuple
from models import Task
from storage import TaskStorage


# Constants for validation
MAX_TITLE_LENGTH = 200
MAX_DESC_LENGTH = 1000


class TaskService:
    """
    Business logic layer for task operations.

    Handles validation, error handling, and task operations
    while maintaining separation from storage and UI concerns.
    """

    def __init__(self, storage: TaskStorage):
        """
        Initialize the TaskService with a storage instance.

        Args:
            storage (TaskStorage): The storage instance to use
        """
        self.storage = storage

    def create_task(self, title: str, description: str = "") -> Tuple[bool, str, Optional[Task]]:
        """
        Create a new task with validation.

        Args:
            title (str): The task title (1-200 characters)
            description (str): The task description (max 1000 characters)

        Returns:
            Tuple[bool, str, Optional[Task]]: (success, message, task_object)
        """
        # Validate title
        if not title:
            return (False, "[ERROR]: Title cannot be empty", None)
        if len(title) < 1 or len(title) > MAX_TITLE_LENGTH:
            return (False, f"[ERROR]: Title must be between 1 and {MAX_TITLE_LENGTH} characters", None)

        # Validate description
        if len(description) > MAX_DESC_LENGTH:
            return (False, f"[ERROR]: Description must be no more than {MAX_DESC_LENGTH} characters", None)

        task = Task(
            id=0,  # Will be set by storage
            title=title,
            description=description
        )
        added_task = self.storage.add(task)
        return (True, f"[OK] Success: Task added successfully! (ID: {added_task.id})", added_task)

    def list_tasks(self) -> List[Task]:
        """
        Get all tasks.

        Returns:
            List[Task]: A list of all task objects
        """
        return self.storage.get_all()

    def update_task(self, task_id: int, title: str = None, description: str = None) -> Tuple[bool, str]:
        """
        Update a task's title or description.

        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title if provided
            description (str, optional): New description if provided

        Returns:
            Tuple[bool, str]: (success, message)
        """
        # Check if task exists
        existing_task = self.storage.get(task_id)
        if existing_task is None:
            return (False, f"[ERROR]: Task not found with ID: {task_id}")

        # Validate title if provided
        if title is not None:
            if not title:
                return (False, "[ERROR]: Title cannot be empty")
            if len(title) < 1 or len(title) > MAX_TITLE_LENGTH:
                return (False, f"[ERROR]: Title must be between 1 and {MAX_TITLE_LENGTH} characters")

        # Validate description if provided
        if description is not None and len(description) > MAX_DESC_LENGTH:
            return (False, f"[ERROR]: Description must be no more than {MAX_DESC_LENGTH} characters")

        # Update the task in storage
        updated_task = self.storage.update(task_id, title, description)
        if updated_task is not None:
            return (True, f"[OK] Success: Task {task_id} updated successfully!")
        else:
            return (False, f"[ERROR]: Failed to update task {task_id}")

    def delete_task(self, task_id: int) -> Tuple[bool, str]:
        """
        Delete a task.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            Tuple[bool, str]: (success, message)
        """
        # Check if task exists
        existing_task = self.storage.get(task_id)
        if existing_task is None:
            return (False, f"[ERROR]: Task not found with ID: {task_id}")

        # Delete the task
        success = self.storage.delete(task_id)
        if success:
            return (True, f"[OK] Success: Task '{existing_task.title}' deleted successfully!")
        else:
            return (False, f"[ERROR]: Failed to delete task {task_id}")

    def toggle_complete(self, task_id: int) -> Tuple[bool, str]:
        """
        Toggle a task's completion status.

        Args:
            task_id (int): The ID of the task to toggle

        Returns:
            Tuple[bool, str]: (success, message)
        """
        # Check if task exists
        existing_task = self.storage.get(task_id)
        if existing_task is None:
            return (False, f"[ERROR]: Task not found with ID: {task_id}")

        # Toggle completion status
        toggled_task = self.storage.toggle_complete(task_id)
        if toggled_task is not None:
            status = "completed" if toggled_task.completed else "not completed"
            return (True, f"[OK] Success: Task {task_id} marked as {status}!")
        else:
            return (False, f"[ERROR]: Failed to toggle task {task_id}")