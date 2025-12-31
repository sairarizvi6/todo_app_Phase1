# Todo Console App - Phase 1

## Description
A Python console application for managing personal todo tasks with a clean, menu-driven interface. This project implements core task management functionality with in-memory storage following spec-driven development principles.

## Features
- ✅ Add Task with title and description
- ✅ View All Tasks with status indicators
- ✅ Update Task details
- ✅ Delete Task with confirmation
- ✅ Toggle Task completion status

## Tech Stack
- Python 3.13+
- UV package manager
- In-memory storage

## Setup Instructions
1. Install UV package manager: `pip install uv`
2. Clone repository: `git clone <repository-url>`
3. Navigate to project directory: `cd todo-console-app`
4. Run the app: `python src/main.py`

## Usage
To run the application:
```bash
python src/main.py
```

The application will display a menu with the following options:
```
=== Todo App Menu ===
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Exit
```

Example interaction:
1. Select "1. Add Task" to create a new task with title and description
2. Select "2. View All Tasks" to see all tasks in a table format with status indicators
3. Select "3. Update Task" to modify an existing task
4. Select "4. Delete Task" to remove a task (with confirmation)
5. Select "5. Toggle Complete" to switch a task's completion status
6. Select "6. Exit" to quit the application

## Project Structure
```
todo-console-app/
├── specs/
│   ├── constitution.md      # Project philosophy and architecture principles
│   └── phase1-spec.md       # Detailed feature specifications
├── src/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # Application entry point
│   ├── models.py            # Task data model with validation
│   ├── storage.py           # In-memory storage implementation
│   ├── service.py           # Business logic layer
│   └── cli.py               # Command-line interface
├── CLAUDE.md                # AI assistant guidelines
├── README.md                # Project documentation
└── pyproject.toml           # UV project configuration
```

## Development
This project follows a spec-driven development approach where all features are defined in detailed specifications before implementation. All code was generated based on these specifications to ensure consistency and adherence to requirements. The architecture maintains proper separation of concerns between models, storage, service, and CLI layers.

## Submission
- Phase: 1 of 5
- Deadline: December , 2026
- Hackathon: Panaversity Hackathon II
