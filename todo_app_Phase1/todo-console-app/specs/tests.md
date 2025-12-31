# Todo Console App - Testing Guide

## Manual Test Cases

### 1. Add Task Feature

#### Test Case 1.1: Add task with valid title only
- **Action**: Select "Add Task" and enter a valid title (1-200 chars)
- **Expected Result**: Task added successfully with auto-generated ID
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 1.2: Add task with valid title and description
- **Action**: Select "Add Task" and enter a valid title and description
- **Expected Result**: Task added successfully with both title and description
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 1.3: Add task with empty title
- **Action**: Select "Add Task" and enter an empty title
- **Expected Result**: Error message "Title cannot be empty"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 1.4: Add task with title longer than 200 characters
- **Action**: Select "Add Task" and enter a title with more than 200 characters
- **Expected Result**: Error message "Title must be between 1 and 200 characters"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 1.5: Add task with description longer than 1000 characters
- **Action**: Select "Add Task" and enter a description with more than 1000 characters
- **Expected Result**: Error message "Description must be no more than 1000 characters"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

### 2. View All Tasks Feature

#### Test Case 2.1: View tasks when no tasks exist
- **Action**: Select "View All Tasks" when no tasks exist
- **Expected Result**: Message "No tasks found."
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 2.2: View tasks with multiple tasks
- **Action**: Select "View All Tasks" when multiple tasks exist
- **Expected Result**: Tasks displayed in table format with ID, Title, Status, and Created date
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 2.3: View tasks with different completion statuses
- **Action**: Select "View All Tasks" with tasks having different completion statuses
- **Expected Result**: Tasks show correct status indicators (✓ Complete, ☐ Pending)
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 2.4: View task summary
- **Action**: Select "View All Tasks" and check summary
- **Expected Result**: Summary shows total, pending, and completed task counts
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

### 3. Update Task Feature

#### Test Case 3.1: Update task title with valid input
- **Action**: Select "Update Task" and enter valid task ID and new title
- **Expected Result**: Task title updated successfully
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 3.2: Update task description with valid input
- **Action**: Select "Update Task" and enter valid task ID and new description
- **Expected Result**: Task description updated successfully
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 3.3: Update task with invalid ID
- **Action**: Select "Update Task" and enter non-existent task ID
- **Expected Result**: Error message "Task not found with ID: [ID]"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 3.4: Update task with empty title
- **Action**: Select "Update Task" and enter empty title
- **Expected Result**: Error message "Title cannot be empty"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 3.5: Update task with title longer than 200 characters
- **Action**: Select "Update Task" and enter title with more than 200 characters
- **Expected Result**: Error message "Title must be between 1 and 200 characters"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 3.6: Update task with description longer than 1000 characters
- **Action**: Select "Update Task" and enter description with more than 1000 characters
- **Expected Result**: Error message "Description must be no more than 1000 characters"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

### 4. Delete Task Feature

#### Test Case 4.1: Delete existing task with confirmation
- **Action**: Select "Delete Task", enter valid task ID, confirm deletion
- **Expected Result**: Task deleted successfully with confirmation message
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 4.2: Delete existing task with cancellation
- **Action**: Select "Delete Task", enter valid task ID, cancel deletion
- **Expected Result**: Task not deleted, operation cancelled
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 4.3: Delete task with invalid ID
- **Action**: Select "Delete Task" and enter non-existent task ID
- **Expected Result**: Error message "Task not found with ID: [ID]"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

### 5. Toggle Complete Feature

#### Test Case 5.1: Toggle completion status of pending task
- **Action**: Select "Toggle Complete" for a pending task
- **Expected Result**: Task status changes from pending to complete
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 5.2: Toggle completion status of completed task
- **Action**: Select "Toggle Complete" for a completed task
- **Expected Result**: Task status changes from complete to pending
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 5.3: Toggle completion status with invalid ID
- **Action**: Select "Toggle Complete" and enter non-existent task ID
- **Expected Result**: Error message "Task not found with ID: [ID]"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

### 6. Menu Navigation

#### Test Case 6.1: Enter valid menu choice
- **Action**: Enter a valid menu choice (1-6)
- **Expected Result**: Corresponding action executed
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 6.2: Enter invalid menu choice (non-numeric)
- **Action**: Enter non-numeric input for menu choice
- **Expected Result**: Error message "Invalid option. Please enter a number between 1-6"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 6.3: Enter invalid menu choice (out of range)
- **Action**: Enter number outside range 1-6
- **Expected Result**: Error message "Invalid option. Please enter a number between 1-6"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Test Case 6.4: Exit application
- **Action**: Select "Exit" (option 6)
- **Expected Result**: Application exits gracefully with goodbye message
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

## Edge Cases

#### Edge Case 1: Empty title input
- **Action**: Enter empty string for title
- **Expected Result**: Validation error "Title cannot be empty"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Edge Case 2: Invalid task ID (non-numeric)
- **Action**: Enter non-numeric input for task ID
- **Expected Result**: Error message "Please enter a valid task ID (number)"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Edge Case 3: Invalid task ID (non-existent)
- **Action**: Enter ID of non-existent task
- **Expected Result**: Error message "Task not found with ID: [ID]"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Edge Case 4: Title with exactly 200 characters
- **Action**: Enter title with exactly 200 characters
- **Expected Result**: Task created successfully
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Edge Case 5: Title with 201 characters
- **Action**: Enter title with 201 characters
- **Expected Result**: Error message "Title must be between 1 and 200 characters"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Edge Case 6: Description with exactly 1000 characters
- **Action**: Enter description with exactly 1000 characters
- **Expected Result**: Task created successfully
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Edge Case 7: Description with 1001 characters
- **Action**: Enter description with 1001 characters
- **Expected Result**: Error message "Description must be no more than 1000 characters"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Edge Case 8: Non-numeric menu choice
- **Action**: Enter non-numeric input for menu choice
- **Expected Result**: Error message "Invalid option. Please enter a number between 1-6"
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Edge Case 9: Ctrl+C handling
- **Action**: Press Ctrl+C during application execution
- **Expected Result**: Application exits gracefully with "Goodbye!" message
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

#### Edge Case 10: Maximum input length for all fields
- **Action**: Enter maximum allowed length for all text fields
- **Expected Result**: All inputs accepted and processed correctly
- **Actual Result**: [To be filled during testing]
- **Status**: [ ] Pass [ ] Fail

## Demo Checklist

### Pre-Demo Setup
- [ ] Ensure application runs without errors
- [ ] Clear any existing test data
- [ ] Prepare sample data for demonstration

### Demo Flow
- [ ] Add multiple tasks with different titles and descriptions
- [ ] View all tasks to show table format and status indicators
- [ ] Update a task title and description
- [ ] Toggle completion status of a task
- [ ] Delete a task with confirmation
- [ ] Show error handling with invalid inputs
- [ ] Exit the application gracefully

### Post-Demo Verification
- [ ] Verify all test cases completed
- [ ] Document actual results
- [ ] Update status for each test case
- [ ] Note any issues or bugs discovered