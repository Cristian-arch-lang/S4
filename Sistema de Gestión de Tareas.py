class TaskManager:
    def _init_(self):
        self.high_priority = Queue()
        self.normal_priority = Queue()

    def add_task(self, task, priority="normal"):
        if priority == "high":
            self.high_priority.enqueue(task)
        else:
            self.normal_priority.enqueue(task)

    def process_task(self):
        if not self.high_priority.is_empty():
            return self.high_priority.dequeue()
        elif not self.normal_priority.is_empty():
            return self.normal_priority.dequeue()
        return "No hay tareas pendientes"

    def show_next_task(self):
        if not self.high_priority.is_empty():
            return self.high_priority.front()
        elif not self.normal_priority.is_empty():
            return self.normal_priority.front()
        return "No hay tareas en la cola"