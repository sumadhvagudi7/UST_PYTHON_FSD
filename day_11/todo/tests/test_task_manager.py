import unittest
import tempfile
import os
from day_11.todo.storage import Storage
from day_11.todo.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False)
        self.filename = self.tmp.name
        self.tmp.close()
        with open(self.filename, 'w') as f:
            f.write('[]')
        self.storage = Storage(self.filename)
        self.manager = TaskManager(self.storage)

    def tearDown(self):
        try:
            os.unlink(self.filename)
        except Exception:
            pass

    def test_add_and_get(self):
        t = self.manager.add_task("task1")
        all_tasks = self.manager.get_all_tasks()
        self.assertEqual(len(all_tasks), 1)
        self.assertEqual(all_tasks[0].id, t.id)

    def test_mark_completed(self):
        t = self.manager.add_task("task2")
        ok = self.manager.mark_completed(t.id)
        self.assertTrue(ok)
        self.assertTrue(self.manager.find_task(t.id).completed)

    def test_delete(self):
        t = self.manager.add_task("task3")
        ok = self.manager.delete_task(t.id)
        self.assertTrue(ok)
        self.assertIsNone(self.manager.find_task(t.id))

    def test_nonexistent_operations(self):
        self.assertFalse(self.manager.mark_completed("no-id"))
        self.assertFalse(self.manager.delete_task("no-id"))