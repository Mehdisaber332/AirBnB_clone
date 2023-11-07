#!/usr/bin/python3
"""importing models for testing"""
import unittest
from models.state import State
from datetime import datetime


class TestUser(unittest.TestCase):
    """TestUser class"""
    def test_state(self):
        """testing instances and their existence"""
        stt = State()
        self.assertTrue(hasattr(stt, "id"))
        self.assertTrue(hasattr(stt, "name"))
        self.assertTrue(hasattr(stt, "created_at"))
        self.assertTrue(hasattr(stt, "updated_at"))
        self.assertIsInstance(stt.id, str)
        self.assertIsInstance(stt.name, str)
        self.assertIsInstance(stt.created_at, datetime)
        self.assertIsInstance(stt.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
