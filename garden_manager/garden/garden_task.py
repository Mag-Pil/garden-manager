class GardenTask:
    def __init__(self, task_name, garden_part, execution_status):
        self.task_name = task_name
        self.garden_part = garden_part
        self.execution_status = execution_status


    def print_garden_task(self):
        print(f"Task name: {self.task_name}")
        print(f"Garden part: {self.garden_part}")
        print(f"Execution status: {self.execution_status}")

