from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.get_database()

experiments = db.experiments
assignments = db.assignments
events = db.events