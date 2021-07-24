from pymongo import MongoClient
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

env = dotenv_values('.env')
MONGO = os.getenv("MONGO")

conn = MongoClient("{MONGO}")