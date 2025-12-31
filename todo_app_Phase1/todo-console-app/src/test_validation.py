"""
Quick test to verify validation in the Task model
"""
from models import Task

print("Testing Task model validation...")

# Test valid task creation
try:
    task = Task(id=1, title="Valid Task", description="This is a valid task description")
    print(f"[OK] Valid task created: {task}")
except Exception as e:
    print(f"[ERROR] Error creating valid task: {e}")

# Test title too long
try:
    long_title = "A" * 201  # 201 characters, exceeding the limit
    invalid_task = Task(id=2, title=long_title)
    print("[ERROR] Failed to catch title length validation")
except ValueError as e:
    print(f"[OK] Correctly caught title validation: {e}")

# Test description too long
try:
    long_desc = "A" * 1001  # 1001 characters, exceeding the limit
    task_with_long_desc = Task(id=3, title="Short Title", description=long_desc)
    print("[ERROR] Failed to catch description length validation")
except ValueError as e:
    print(f"[OK] Correctly caught description validation: {e}")

print("Validation tests completed!")