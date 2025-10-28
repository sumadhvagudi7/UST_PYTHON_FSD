import json
from typing import List, Dict

class Storage:
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename

    def save(self, tasks: List[Dict]) -> None:
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2)

    def load(self) -> List[Dict]:
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            # Corrupt file -> return empty list
            return []