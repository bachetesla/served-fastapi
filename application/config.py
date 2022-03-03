"""
This is config file for the application.
"""
from os import environ
from dotenv import load_dotenv
from __types.db import Postgresql

# Load environment variables from .env file
load_dotenv()

DEBUG = True

DATABASE = Postgresql(
   username=environ.get("POSTGRES_USER"),
   password=environ.get("POSTGRES_PASSWORD"),
   host=environ.get("POSTGRES_HOST"),
   port=environ.get("POSTGRES_PORT"),
   db=environ.get("POSTGRES_DB"),
)
