class GardenTask:
    def __init__(self, task_name, garden_part, execution_status):
        self.task_name = task_name
        self.garden_part = garden_part
        self.execution_status = execution_status


def print_garden_task(garden_task):
    print(f"Task name: {garden_task.task_name}")
    print(f"Garden part: {garden_task.garden_part}")
    print(f"Execution status: {garden_task.execution_status}")

