#!/usr/bin/python3
"""importing models"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
