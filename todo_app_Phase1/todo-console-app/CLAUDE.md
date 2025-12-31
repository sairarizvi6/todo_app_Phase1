# Todo App - Development Guide

## Project Overview
This is a spec-driven Python console app using in-memory storage. The application follows clean architecture principles with proper separation of concerns between models, storage, service, and CLI layers.

## Spec-Kit Structure
- `/specs/constitution.md` - Project philosophy, coding standards, and architecture principles
- `/specs/phase1-spec.md` - Detailed feature specifications for Phase 1

## Architecture
The application follows a layered architecture:
`models.py` → `storage.py` → `service.py` → `cli.py` → `main.py`

- **models.py**: Defines the Task data model with validation
- **storage.py**: Handles in-memory storage operations
- **service.py**: Implements business logic and validation
- **cli.py**: Provides the command-line interface
- **main.py**: Application entry point

## How to Use Specs
1. Read the relevant specification document before implementing any feature
2. Reference the specification in your prompts with `@specs/phase1-spec.md`
3. Update specifications if requirements change during development
4. Ensure all code aligns with the specifications

## Development Workflow
1. Write or update specification in `/specs` directory
2. Generate code based on the specification
3. Test functionality manually or with automated tests
4. Refine specification if needed based on implementation challenges
5. Regenerate code if specifications change

## Running the App
```bash
python src/main.py
```

## Testing Checklist
- [ ] Add task with title only
- [ ] Add task with title + description
- [ ] View empty task list
- [ ] View tasks with data
- [ ] Update task title
- [ ] Update task description
- [ ] Delete task with confirmation
- [ ] Toggle task status
- [ ] Handle invalid inputs
- [ ] Exit gracefully

## Code Standards
- Follow PEP 8 style guide
- Include type hints for all functions and methods
- Add comprehensive docstrings to all classes and functions
- Implement proper error handling with user-friendly messages
- Maintain separation of concerns between layers
- Use constants for validation values (e.g., MAX_TITLE_LENGTH)

## Key Constants
- `MAX_TITLE_LENGTH = 200` - Maximum length for task titles
- `MAX_DESC_LENGTH = 1000` - Maximum length for task descriptions

## Return Format Requirements
All service methods should return `(success: bool, message: str, data: Optional)`:
- Success: `(True, "[OK] Success message", task_object)`
- Error: `(False, "[ERROR] Error message", None)`