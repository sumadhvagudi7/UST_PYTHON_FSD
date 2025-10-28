import unittest
from day_11.todo.task import Task

class TestTask(unittest.TestCase):
    def test_create_and_to_from_dict(self):
        t = Task.create("my task")
        d = t.to_dict()
        self.assertIn("id", d)
        self.assertEqual(d["description"], "my task")
        t2 = Task.from_dict(d)
        self.assertEqual(t.id, t2.id)
        self.assertEqual(t.description, t2.description)

    def test_empty_description_raises(self):
        with self.assertRaises(ValueError):
            Task.create("")