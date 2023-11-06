#!/usr/bin/env python3
from uuid import uuid4 as id
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                time = datetime.now().isoformat()
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.fromisoformat(
                        time)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.fromisoformat(
                        time)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(id())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
