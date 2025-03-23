El sistema procesa primero las tareas urgentes y, cuando estas terminan, atiende las tareas normales.

Código del gestor de tareas:

class TaskManager:
    """Gestor de tareas con prioridad."""
    def _init_(self):
        self.high_priority = Queue()  # Tareas urgentes
        self.normal_priority = Queue()  # Tareas normales

    def add_task(self, task, priority="normal"):
        """Agrega una tarea con prioridad alta o normal."""
        if priority == "alta":
            self.high_priority.enqueue(task)
        else:
            self.normal_priority.enqueue(task)

    def process_task(self):
        """Procesa la siguiente tarea en orden de prioridad."""
        if not self.high_priority.is_empty():
            return f"Tarea urgente atendida: {self.high_priority.dequeue()}"
        elif not self.normal_priority.is_empty():
            return f"Tarea normal atendida: {self.normal_priority.dequeue()}"
        else:
            return "No hay tareas pendientes."