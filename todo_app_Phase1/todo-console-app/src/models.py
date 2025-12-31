"""
Todo Console Application - Data Models

This module defines the data models for the todo application.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


# Validation constants
MAX_TITLE_LENGTH = 200
MAX_DESC_LENGTH = 1000


@dataclass
class Task:
    """
    Represents a single task in the todo list.

    Attributes:
        id (int): Auto-incrementing identifier, starts from 1
        title (str): Required title, 1-200 characters
        description (str): Optional description, max 1000 characters
        completed (bool): Completion status, default False
        created_at (datetime): Auto-generated timestamp on creation
        updated_at (datetime): Auto-updated timestamp on modification
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        """
        Initialize timestamps if not provided.

        Validates that the title and description meet length requirements.
        """
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()

        # Validate title length
        if not (1 <= len(self.title) <= MAX_TITLE_LENGTH):
            raise ValueError(f"Title must be between 1 and {MAX_TITLE_LENGTH} characters")

        # Validate description length
        if len(self.description) > MAX_DESC_LENGTH:
            raise ValueError(f"Description must be no more than {MAX_DESC_LENGTH} characters")

    def mark_completed(self):
        """
        Mark the task as completed and set the completion timestamp.
        """
        self.completed = True
        self.updated_at = datetime.now()

    def update_content(self, title: Optional[str] = None, description: Optional[str] = None):
        """
        Update task content and update the modification timestamp.

        Args:
            title (Optional[str]): New title if provided
            description (Optional[str]): New description if provided

        Raises:
            ValueError: If title length is invalid
        """
        if title is not None:
            if not (1 <= len(title) <= MAX_TITLE_LENGTH):
                raise ValueError(f"Title must be between 1 and {MAX_TITLE_LENGTH} characters")
            self.title = title
        if description is not None:
            if len(description) > MAX_DESC_LENGTH:
                raise ValueError(f"Description must be no more than {MAX_DESC_LENGTH} characters")
            self.description = description
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of the task.

        Returns:
            str: Formatted string with completion status, ID, and title
        """
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}: {self.title}"