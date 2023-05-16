from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os


# Create Flask app
app = Flask(__name__)

# Connect to MongoDB
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client['python_learn']

# Import routes
from app import routes
