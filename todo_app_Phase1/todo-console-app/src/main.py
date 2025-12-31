"""
Todo Console Application - Entry Point

This is the main entry point for the todo console application.
"""
from storage import TaskStorage
from service import TaskService
from cli import TodoCLI


def main():
    """
    Main function to start the todo application.

    Initializes components and starts the CLI loop,
    maintaining separation from business logic and storage.
    Handles Ctrl+C gracefully.
    """
    print("Welcome to the Todo Console Application!")

    try:
        # Initialize TaskStorage
        storage = TaskStorage()

        # Initialize TaskService with storage
        service = TaskService(storage)

        # Initialize TodoCLI with the same service and storage instances
        cli = TodoCLI(service=service, storage=storage)

        # Start CLI loop
        cli.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Goodbye!")


if __name__ == "__main__":
    main()