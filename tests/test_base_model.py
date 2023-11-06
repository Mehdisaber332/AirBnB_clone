#!/usr/bin/env python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

    def test_str(self):
        my_model = BaseModel()
        magic_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), magic_str)

    def test_save(self):
        my_model = BaseModel()
        current_time = my_model.updated_at
        my_model.save()


