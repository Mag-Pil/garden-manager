class GardenTask:
    def __init__(self, task_name, garden_part, execution_status):
        self.task_name = task_name
        self.garden_part = garden_part
        self.execution_status = execution_status


    def __str__(self):
        return (
            f"Task name: {self.task_name}\n"
            f"Garden part: {self.garden_part}\n"
            f"Execution status: {self.execution_status}"
        )

