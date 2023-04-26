from general.exercise import Exercise


def print_task(task_name):
    """Authenticates on AI Devs, and prints exercise description"""
    exercise_obj = Exercise(task_name)
    exercise_obj.print_task()
