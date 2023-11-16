#!/usr/bin/python3
"""importing models for testing"""
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """TestReview class"""
    def test_review(self):
        """review test cases"""
        rev = Review()

        self.assertTrue(hasattr(rev, "id"))
        self.assertTrue(isinstance(rev.id, str))

        self.assertTrue(hasattr(rev, "created_at"))
        self.assertTrue(isinstance(rev.created_at, datetime))

        self.assertTrue(hasattr(rev, "updated_at"))
        self.assertTrue(isinstance(rev.updated_at, datetime))

        self.assertTrue(hasattr(rev, "place_id"))
        self.assertTrue(isinstance(rev.place_id, str))

        self.assertTrue(hasattr(rev, "user_id"))
        self.assertTrue(isinstance(rev.user_id, str))

        self.assertTrue(hasattr(rev, "text"))
        self.assertTrue(isinstance(rev.text, str))

        self.assertEqual(rev.user_id, "")
        self.assertEqual(rev.place_id, "")
        self.assertEqual(rev.text, "")


if __name__ == "__main__":
    unittest.main()
