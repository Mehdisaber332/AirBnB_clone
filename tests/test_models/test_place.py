#!/usr/bin/python3
"""importing models"""
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """TestPlace class"""
    def test_place(self):
        """place test cases"""
        plc = Place()

        self.assertTrue(hasattr(plc, "id"))
        self.assertIsInstance(plc.id, str)

        self.assertTrue(hasattr(plc, "created_at"))
        self.assertIsInstance(plc.created_at, datetime)

        self.assertTrue(hasattr(plc, "updated_at"))
        self.assertIsInstance(plc.updated_at, datetime)

        self.assertTrue(hasattr(plc, "city_id"))
        self.assertIsInstance(plc.city_id, str)

        self.assertTrue(hasattr(plc, "user_id"))
        self.assertIsInstance(plc.user_id, str)

        self.assertTrue(hasattr(plc, "name"))
        self.assertIsInstance(plc.name, str)

        self.assertTrue(hasattr(plc, "description"))
        self.assertIsInstance(plc.description, str)

        self.assertTrue(hasattr(plc, "number_rooms"))
        self.assertIsInstance(plc.number_rooms, int)

        self.assertTrue(hasattr(plc, "number_bathrooms"))
        self.assertIsInstance(plc.number_bathrooms, int)

        self.assertTrue(hasattr(plc, "max_guest"))
        self.assertIsInstance(plc.max_guest, int)

        self.assertTrue(hasattr(plc, "price_by_night"))
        self.assertIsInstance(plc.price_by_night, int)

        self.assertTrue(hasattr(plc, "latitude"))
        self.assertIsInstance(plc.latitude, float)

        self.assertTrue(hasattr(plc, "longitude"))
        self.assertIsInstance(plc.longitude, float)

        self.assertTrue(hasattr(plc, "amenity_ids"))
        self.assertIsInstance(plc.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
