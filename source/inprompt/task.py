from general.print_task import print_task
import os

if __name__ == "__main__":
    task_name = __file__.split(os.sep)[-2]
    print_task(task_name)
