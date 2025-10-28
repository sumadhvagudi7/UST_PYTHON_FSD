from typing import List, Optional
from task import Task
from storage import Storage

class TaskManager:
    def __init__(self, storage: Optional[Storage] = None):
        self.storage = storage or Storage()
        self.tasks: List[Task] = []
        self._load()

    def _load(self) -> None:
        raw = self.storage.load()
        self.tasks = [Task.from_dict(d) for d in raw]

    def _save(self) -> None:
        self.storage.save([t.to_dict() for t in self.tasks])

    def add_task(self, description: str) -> Task:
        task = Task.create(description)
        self.tasks.append(task)
        self._save()
        return task

    def get_all_tasks(self) -> List[Task]:
        return list(self.tasks)

    def find_task(self, task_id: str) -> Optional[Task]:
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def mark_completed(self, task_id: str) -> bool:
        task = self.find_task(task_id)
        if not task:
            return False
        if not task.completed:
            task.completed = True
            self._save()
        return True

    def delete_task(self, task_id: str) -> bool:
        task = self.find_task(task_id)
        if not task:
            return False
        self.tasks.remove(task)
        self._save()
        return True