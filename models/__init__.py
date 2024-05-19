#!/usr/bin/env python3
"""Import Filestorage autoinit for models package."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
