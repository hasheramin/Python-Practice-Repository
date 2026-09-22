# A Program to manage tasks for a task management application

def add_task(tasks, task):
    tasks.append(task)


def complete_task(tasks, title):
    for task in tasks:
        if task.title.lower() == title.lower():
            task.complete()
            return True

    return False


def display_tasks(tasks):
    for task in tasks:
        task.display()
