#!/usr/bin/python3
"""magic method so it all works"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
