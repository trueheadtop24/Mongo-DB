from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username='aacuser', password='SNHU1234', host='nv-desktop-services.apporto.com', port=31580, db='aac', collection='animals'):
        try:
            self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/')
            self.database = self.client[db]
            self.collection = self.database[collection]
            print("Connected to MongoDB.")
        except ConnectionFailure as e:
            print(f"Connection error: {e}")

    def create(self, data):
        """Insert a document into the collection"""
        if data is not None and isinstance(data, dict):
            result = self.collection.insert_one(data)
            return True if result.acknowledged else False
        else:
            raise Exception("Invalid data. Must be a non-empty dictionary.")

    def read(self, query):
        """Read documents matching the query"""
        if query is not None and isinstance(query, dict):
            results = list(self.collection.find(query))
            return results
        else:
            raise Exception("Invalid query. Must be a dictionary.")
