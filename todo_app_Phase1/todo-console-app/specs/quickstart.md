# Quickstart Guide for CLI Todo Manager

## Prerequisites
- Python 3.8 or higher installed on your system

## Installation
1. Clone or download the project repository
2. Navigate to the project directory
3. Ensure you have Python 3.8+ installed (`python --version`)

## Running the Application
1. Navigate to the project root directory
2. Run the application: `python -m src.main`
3. The CLI interface will start and display the main menu

## Basic Usage
Once the application is running, you'll see a menu with the following options:
1. Add Task
2. View Task List
3. View Task Details
4. Update Task
5. Delete Task
6. Mark Task Complete/Incomplete
7. Exit

### Adding a Task
1. Select option 1 from the menu
2. Enter the task title (1-200 characters)
3. Optionally enter a task description (max 1000 characters)
4. The system will confirm the task was added with its ID

### Viewing Task List
1. Select option 2 from the menu
2. The system will display all tasks in a formatted table
3. Shows ID, Title, Status (✓/☐), and Created Date
4. Displays summary statistics (total, pending, completed tasks)

### Viewing Task Details
1. Select option 3 from the menu
2. Enter the task ID you want to view
3. The system will display detailed information about the task

### Updating a Task
1. Select option 4 from the menu
2. Enter the task ID you want to update
3. Enter the new title (or press Enter to keep current)
4. Enter the new description (or press Enter to keep current)
5. The system will confirm the update

### Deleting a Task
1. Select option 5 from the menu
2. Enter the task ID you want to delete
3. Confirm the deletion when prompted
4. The system will confirm the deletion

### Marking Task Complete/Incomplete
1. Select option 6 from the menu
2. Enter the task ID you want to toggle
3. The system will toggle the completion status
4. The system will confirm the new status

## Exiting the Application
Select option 7 from the menu or use Ctrl+C to exit the application.