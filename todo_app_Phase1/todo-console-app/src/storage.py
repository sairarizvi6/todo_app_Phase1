"""
Todo Console Application - Storage

This module handles the in-memory storage of tasks.
"""
from typing import Dict, List, Optional
from models import Task
from datetime import datetime


class TaskStorage:
    """
    In-memory storage layer for tasks.

    Provides CRUD operations and maintains tasks in a dictionary with auto-incrementing IDs.
    """

    def __init__(self):
        """Initialize the in-memory storage with an empty task dictionary."""
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def add(self, task: Task) -> Task:
        """
        Add a new task to storage with an auto-incremented ID.

        Args:
            task (Task): The task object to add

        Returns:
            Task: The added task with updated ID
        """
        task_id = self._next_id
        self._next_id += 1
        task.id = task_id
        task.created_at = datetime.now()
        task.updated_at = datetime.now()
        self._tasks[task_id] = task
        return task

    def get(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[Task]: The task object if found, None otherwise
        """
        return self._tasks.get(task_id)

    def get_all(self) -> List[Task]:
        """
        Get all tasks.

        Returns:
            List[Task]: A list of all task objects
        """
        return list(self._tasks.values())

    def update(self, task_id: int, title: str = None, description: str = None) -> Optional[Task]:
        """
        Update a task's title or description.

        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task

        Returns:
            Optional[Task]: The updated task if found, None otherwise
        """
        task = self._tasks.get(task_id)
        if task is None:
            return None

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        task.updated_at = datetime.now()
        return task

    def delete(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def toggle_complete(self, task_id: int) -> Optional[Task]:
        """
        Toggle a task's completion status.

        Args:
            task_id (int): The ID of the task to toggle

        Returns:
            Optional[Task]: The updated task if found, None otherwise
        """
        task = self._tasks.get(task_id)
        if task is None:
            return None

        task.completed = not task.completed
        task.updated_at = datetime.now()
        return task