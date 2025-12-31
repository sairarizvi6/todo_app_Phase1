# Todo Console App - Phase 1 Specification

## Overview
Phase 1 of the Todo Console Application will implement the core functionality for managing personal todo tasks through a command-line interface, following the architecture and standards defined in the constitution.

## Clarifications
### Session 2025-12-30
- Q: Should we track creation/modification timestamps? → A: Yes
- Q: Should we use numbered menu or command-based interface? → A: Command-based interface
- Q: Should completed tasks be hidden by default or shown with strikethrough? → A: All tasks visible with strikethrough
- Q: What validation approach should we use? → A: Basic validation (non-empty title required)
- Q: Should we have a confirmation prompt before deleting tasks? → A: Yes

## Features

### 1. Add Task
- **Input**: Title (required), Description (optional)
- **Validation**:
  - Title: 1-200 characters, cannot be empty
  - Description: max 1000 characters
- **Output**: Confirmation with auto-generated Task ID
- **Error Handling**: Empty title, invalid characters

### 2. View Task List
- **Display**: ID, Title, Status (✓/☐), Created Date
- **Format**: Clean table or structured list
- **Empty State**: Friendly message when no tasks exist
- **Summary**: Show count (total, pending, completed)

### 3. Update Task
- **Input**: Task ID + (new title OR new description)
- **Validation**: Task ID must exist
- **Output**: Confirmation of updated fields
- **Error Handling**: Invalid ID, empty input

### 4. Delete Task
- **Input**: Task ID
- **Validation**: Task ID must exist
- **Confirmation**: Ask "Are you sure? (y/n)"
- **Output**: Confirmation message with deleted task title
- **Error Handling**: Invalid ID, invalid confirmation

### 5. Mark as Complete
- **Input**: Task ID
- **Toggle**: Pending → Complete OR Complete → Pending
- **Output**: Confirmation with new status
- **Error Handling**: Invalid ID

## Data Model
- **Task**: Each task has:
  - ID (auto-incrementing, starts from 1)
  - Title (required, 1-200 characters)
  - Description (optional, max 1000 characters)
  - Completion status (boolean, default: False)
  - Creation timestamp (auto-generated on creation)
  - Update timestamp (auto-updated on modification)

## Architecture Implementation

### 1. Models Layer (`models.py`)
- Define Task dataclass with validation
- Include type hints and docstrings
- Follow PEP 8 compliance

### 2. Storage Layer (`storage.py`)
- Implement in-memory storage using Python dictionaries
- Provide CRUD operations on task dictionary
- Include type hints and docstrings
- Follow PEP 8 compliance

### 3. Service Layer (`service.py`)
- Implement business logic for task operations
- Include validation and error handling
- Include type hints and docstrings
- Follow PEP 8 compliance

### 4. CLI Layer (`cli.py`)
- Implement menu-driven command-line interface
- Provide clear prompts and feedback
- Handle input validation and error messages
- Include type hints and docstrings
- Follow PEP 8 compliance

### 5. Main (`main.py`)
- Initialize components and start CLI loop
- Include type hints and docstrings
- Follow PEP 8 compliance

## Technical Requirements
- Python 3.13+
- No external dependencies beyond standard library
- Type hints on all functions
- Docstrings on all classes/functions
- PEP 8 compliant code
- Proper separation of concerns
- No hardcoded values (use constants)

## User Experience Requirements
- Menu design with options 1-6 as specified in constitution
- Clear prompts and immediate feedback
- Visual indicators (✓ for complete, ☐ for pending)
- Specific and actionable error messages
- Graceful exit handling

## Error Handling Requirements
- Menu choice validation (must be 1-6, handle non-numeric input)
- Task ID validation (must be integer, must exist in storage)
- Title validation (must not be empty, max 200 chars)
- Description validation (max 1000 chars)
- Proper error message format as specified in constitution

## Acceptance Criteria
1. User can successfully add a new task with title (1-200 chars) and optional description
2. User can view all tasks with clear indication of completion status and creation date
3. User can update existing task title or description
4. User can mark tasks as completed and see the status update
5. User can mark completed tasks as not completed
6. User can delete tasks from the list with confirmation
7. Application handles invalid inputs gracefully with appropriate error messages
8. Application provides clear feedback for all operations
9. All functions have proper type hints and docstrings
10. Code follows PEP 8 style guide
11. Architecture follows the specified layer separation
12. Error messages follow the format specified in the constitution