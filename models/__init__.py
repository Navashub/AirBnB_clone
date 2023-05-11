#!/usr/bin/python3
"""__init__ dunder method for the models dir."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
