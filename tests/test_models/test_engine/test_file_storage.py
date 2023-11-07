#!/usr/bin/python3
"""importing models for testing"""
import unittest
import os
import json
import models
from models.base_model import BaseModel
from models import storage


class TestStorageFile(unittest.TestCase):
    def setUp(self):
        self.file_path = storage._FileStorage__file_path
        self.inst = BaseModel()
        self.obj = storage._FileStorage__objects
        self.key = "BaseModel" + self.inst.id

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def TestAll(self):
        res = storage.all()
        self.assertEqual(res, self.obj)

    def TestNew(self):
        self.storage.new(self.obj)
        k = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.assertIn(k, self.obj)

    def TestSaveReload(self):
        self.storage.new(self.obj)
        self.storage.save()
        self.storage.reload()
        k = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.assertIn(k, self.storage.all())
        self.assertEqual(self.storage.all()[k].id, self.obj.id)


if __name__ == "__main__":
    unittest.main()
