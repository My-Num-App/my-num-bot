import pymongo
import src.config.general as conf

DB_NAME = 'my_num'
COLLECTION_NAME = 'phone_numbers'


class DatabaseService:
    def __init__(self):
        client = pymongo.MongoClient(conf.MONGO_CONNECTION_STRING)
        self.client = client
        self.col = self.create_collection()

    def create_db(self):
        db = self.client[DB_NAME]
        return db

    def create_collection(self):
        db = self.create_db()
        col = db[COLLECTION_NAME]
        col.create_index('numbers', unique=True)
        return col

    def insert_one(self, data):
        try:
            self.col.insert_one(data)
        except:
            print('Unique One')

    def is_db_exists(self):
        db_list = self.client.list_database_names()
        if DB_NAME in db_list:
            return True
        return False
