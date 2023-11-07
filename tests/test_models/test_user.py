#!/usr/bin/python3
"""importing models for testing"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """User test class"""
    def test_user(self):
        """testing existence and attributes"""

        usr = User()

        self.assertTrue(hasattr(usr, "id"))
        self.assertTrue(isinstance(usr.id, str))

        self.assertTrue(hasattr(usr, "created_at"))
        self.assertTrue(isinstance(usr.created_at, datetime))

        self.assertTrue(hasattr(usr, "updated_at"))
        self.assertTrue(isinstance(usr.updated_at, datetime))

        self.assertTrue(hasattr(usr, "email"))
        self.assertTrue(isinstance(usr.email, str))

        self.assertTrue(hasattr(usr, "password"))
        self.assertTrue(isinstance(usr.password, str))

        self.assertTrue(hasattr(usr, "first_name"))
        self.assertTrue(isinstance(usr.first_name, str))

        self.assertTrue(hasattr(usr, "last_name"))
        self.assertTrue(isinstance(usr.last_name, str))

        self.assertEqual(usr.email, "")
        self.assertEqual(usr.password, "")
        self.assertEqual(usr.first_name, "")
        self.assertEqual(usr.last_name, "")


if __name__ == "__main__":
    unittest.main()
