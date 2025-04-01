from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from constants import Constant  

def mongo_connect():
    try:
        client = MongoClient(Constant.uri.value, server_api=ServerApi('1'))    
        client.admin.command('ping')
        print("Correctly connected to the database")
        return client.get_database(Constant.db_name.value)    # can be added with read and write access
    except Exception as e:
        print(e)
        return None
    
    
def get_collection(collection_name):
    db = mongo_connect()    # add with lazy loading
    if db is not None:
        return db.get_collection(collection_name)
    print("Error connecting to the database")
    return None

# class CRUDOperations:
#     def __init__(self, uri, db_name, collection_name):
#         self.connection = MongoDBConnection()  
#         self.db = self.connection.connect(uri, db_name)  
#         self.active_collection = self.connection.get_collection(collection_name) 

#     def create(self, document):
#         collection = self.active_collection
#         if collection is not None:
#             result = collection.insert_one(document)  
#             return result.inserted_id  
#         return None

#     def read(self, query):
#         collection = self.active_collection
#         if collection is not None:
#             return collection.find(query)  
#         return None

#     def update(self, query, update_values):
#         collection = self.active_collection
#         if collection is not None:
#             result = collection.update_one(query, {"$set": update_values})  
#             return result.modified_count  
#         return 0

#     def delete(self, query):
#         """
#         Delete documents from the collection based on a query.
#         """
#         collection = self.active_collection
#         if collection is not None:
#             result = collection.delete_one(query) 
#             return result.deleted_count  
#         return 0