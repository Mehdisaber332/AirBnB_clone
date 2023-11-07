#!/usr/bin/env python3
"""import models for test"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class from unittest, Test case"""

    def test_init(self):
        """initialization test class"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertEqual(len(my_model.id), 36)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """Test magic str format"""
        my_model = BaseModel()
        magic_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), magic_str)

    def test_save(self):
        """Test save method"""
        my_model = BaseModel()
        current_time = my_model.updated_at
        my_model.save()

    def test_to_dict(self):
        """Test dict method"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        self.assertIsInstance(my_model_json, dict)
        self.assertEqual(my_model_json["name"], my_model.name)
        self.assertEqual(my_model_json["my_number"], my_model.my_number)
        self.assertEqual(my_model_json["id"], my_model.id)
        self.assertEqual(my_model_json["__class__"], "BaseModel")
        self.assertEqual(my_model_json["created_at"]
                         [:-7], my_model.created_at.isoformat()[:-7])
        self.assertEqual(my_model_json["updated_at"]
                         [:-7], my_model.updated_at.isoformat()[:-7])


if __name__ == "__main__":
    unittest.main()
