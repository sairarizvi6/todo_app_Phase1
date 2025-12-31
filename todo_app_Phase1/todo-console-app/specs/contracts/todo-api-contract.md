# CLI Todo Manager API Contracts

## Task Operations

### Add Task
- **Command**: `add`
- **Arguments**:
  - `title` (str, required): Task title (1-200 characters)
  - `description` (str, optional): Task description (max 1000 characters)
- **Output**: 
  - Success: "Task added successfully with ID: {id}"
  - Error: "Error: {error_message}"
- **Validation**:
  - Title must be 1-200 characters
  - Description must be max 1000 characters if provided

### List Tasks
- **Command**: `list`
- **Arguments**: None
- **Output**:
  - Success: Formatted table with columns [ID, Title, Status, Created Date]
  - Empty state: "No tasks found."
  - Summary: "Total: {total}, Pending: {pending}, Completed: {completed}"
- **Validation**: None

### View Task
- **Command**: `view`
- **Arguments**:
  - `id` (int, required): Task ID
- **Output**:
  - Success: Detailed view of task with all fields
  - Error: "Error: {error_message}"
- **Validation**:
  - ID must exist in storage

### Update Task
- **Command**: `update`
- **Arguments**:
  - `id` (int, required): Task ID
  - `title` (str, optional): New title (1-200 characters)
  - `description` (str, optional): New description (max 1000 characters)
- **Output**:
  - Success: "Task {id} updated successfully"
  - Error: "Error: {error_message}"
- **Validation**:
  - ID must exist in storage
  - If title provided, must be 1-200 characters
  - If description provided, must be max 1000 characters

### Delete Task
- **Command**: `delete`
- **Arguments**:
  - `id` (int, required): Task ID
- **Output**:
  - Success: "Task '{title}' deleted successfully" (with confirmation prompt)
  - Error: "Error: {error_message}"
- **Validation**:
  - ID must exist in storage
  - User must confirm deletion with 'y' or 'yes'

### Mark Task Complete
- **Command**: `complete`
- **Arguments**:
  - `id` (int, required): Task ID
- **Output**:
  - Success: "Task {id} marked as complete"
  - Error: "Error: {error_message}"
- **Validation**:
  - ID must exist in storage

### Mark Task Incomplete
- **Command**: `incomplete`
- **Arguments**:
  - `id` (int, required): Task ID
- **Output**:
  - Success: "Task {id} marked as incomplete"
  - Error: "Error: {error_message}"
- **Validation**:
  - ID must exist in storage