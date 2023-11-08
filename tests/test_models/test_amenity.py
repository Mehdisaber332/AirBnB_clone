#!/usr/bin/python3
"""importing models for testing"""
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Amenity test class"""
    def test_amenity(self):
        """amenity test cases"""
        amnt = Amenity()
        self.assertTrue(hasattr(amnt, "id"))
        self.assertTrue(hasattr(amnt, "name"))
        self.assertTrue(hasattr(amnt, "created_at"))
        self.assertTrue(hasattr(amnt, "updated_at"))
        self.assertIsInstance(amnt.id, str)
        self.assertIsInstance(amnt.name, str)
        self.assertIsInstance(amnt.created_at, datetime)
        self.assertIsInstance(amnt.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
