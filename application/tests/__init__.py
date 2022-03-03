"""
This is tests, a test suite for the application.
"""

from fastapi.testclient import TestClient
from application.main import app

client = TestClient(app)

