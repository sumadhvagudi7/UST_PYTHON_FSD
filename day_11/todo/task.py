from dataclasses import dataclass, asdict
from typing import Dict
import datetime
import uuid

@dataclass
class Task:
    id: str
    description: str
    completed: bool = False
    created_at: str = None

    def __post_init__(self):
        if self.created_at is None:
            # ISO format timestamp
            self.created_at = datetime.datetime.utcnow().isoformat()

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict) -> "Task":
        return Task(
            id=data["id"],
            description=data["description"],
            completed=data.get("completed", False),
            created_at=data.get("created_at"),
        )

    @staticmethod
    def create(description: str) -> "Task":
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")
        return Task(id=str(uuid.uuid4()), description=description.strip())