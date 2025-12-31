# Data Model Specification for CLI Todo Manager

## Task Entity

### Fields
- **id** (int): Auto-incrementing unique identifier, starts from 1
- **title** (str): Required field, 1-200 characters
- **description** (str): Optional field, max 1000 characters
- **completed** (bool): Task completion status, default False
- **created_at** (datetime): Auto-generated timestamp when task is created
- **updated_at** (datetime): Auto-updated timestamp when task is modified

### Validation Rules
- **id**: Must be a positive integer, auto-generated
- **title**: Required, 1-200 characters, cannot be empty or whitespace-only
- **description**: Optional, max 1000 characters, can be empty
- **completed**: Boolean value, default False
- **created_at**: Auto-generated on creation, immutable after creation
- **updated_at**: Auto-updated on any modification

### State Transitions
- **completed**: Can transition from False to True (mark complete) or True to False (mark incomplete)

## Storage Model

### In-Memory Storage Structure
- **tasks** (dict): Dictionary with task ID as key and Task object as value
- **next_id** (int): Counter for the next available task ID, starts from 1

### Relationships
- No relationships between entities in this simple model