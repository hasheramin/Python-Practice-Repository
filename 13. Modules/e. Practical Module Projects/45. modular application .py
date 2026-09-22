# A Program to build a modular task management application for adding, completing, and displaying tasks

from task_manager import Task, add_task, complete_task, display_tasks

tasks = []

add_task(tasks, Task("Learn Python Modules"))
add_task(tasks, Task("Practice Packages"))
add_task(tasks, Task("Build a Python Project"))

complete_task(tasks, "Practice Packages")

print("\nTask List:")
display_tasks(tasks)

# Explanation:
# The task_manager package separates task data from task operations.
# Task stores information about an individual task.
# manager.py handles adding, completing, and displaying tasks.
# The main program coordinates all components.
# This demonstrates how modules and packages can work together to create a maintainable application.

# Real-Life Use:
# The same architecture can be expanded into project management, to-do applications, issue trackers, and productivity software.