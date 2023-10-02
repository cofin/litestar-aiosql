"""Metadata for the Project."""
from __future__ import annotations

import importlib.metadata

__all__ = ["__version__", "__project__"]

__version__ = importlib.metadata.version("aiosql_litestar")
"""Version of the project."""
__project__ = importlib.metadata.metadata("aiosql_litestar")["Name"]
"""Name of the project."""
