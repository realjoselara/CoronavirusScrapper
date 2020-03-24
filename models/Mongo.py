''' Mongo class ussed as interface to pyMongo ''' 

from pymongo import MongoClient
import os

class Mongo:
    ''' Stores the model information and act as interface for PyMongo '''

    MONGO_URL = 'mongodb://localhost:27017/'
    DATABASE_NAME = 'coronavirus'
    # MONGO_URL = os.environ.get('MONGO_URL')

    def __init__(self, url=MONGO_URL, database_name=DATABASE_NAME):
        if not isinstance(url, str) and not isinstance(database_name, str):
            raise TypeError

        if not url and not database_name:
            raise Exception('Missing argument')

        self.url = url
        self.client = MongoClient(self.url)
        self.db = self.client[database_name]

    def connection_client(self):
        return self.db

