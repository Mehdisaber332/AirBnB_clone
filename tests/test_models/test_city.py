#!/usr/bin/python3
"""importing models for testing"""
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """TestCity class"""
    def test_city(self):
        """testing instances and their existence"""
        ct = City()
        self.assertTrue(hasattr(ct, "id"))
        self.assertTrue(hasattr(ct, "name"))
        self.assertTrue(hasattr(ct, "state_id"))
        self.assertTrue(hasattr(ct, "created_at"))
        self.assertTrue(hasattr(ct, "updated_at"))

        self.assertIsInstance(ct.id, str)
        self.assertIsInstance(ct.name, str)
        self.assertIsInstance(ct.state_id, str)
        self.assertIsInstance(ct.created_at, datetime)
        self.assertIsInstance(ct.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
