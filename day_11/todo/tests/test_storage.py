import unittest
import tempfile
import os
from day_11.todo.storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False)
        self.filename = self.tmp.name
        self.tmp.close()
        # ensure file starts empty
        with open(self.filename, 'w') as f:
            f.write('[]')

    def tearDown(self):
        try:
            os.unlink(self.filename)
        except Exception:
            pass

    def test_save_and_load(self):
        s = Storage(self.filename)
        data = [{"id": "1", "description": "a"}]
        s.save(data)
        loaded = s.load()
        self.assertEqual(loaded, data)