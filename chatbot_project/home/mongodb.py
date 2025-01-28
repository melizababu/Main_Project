

from pymongo import MongoClient

def get_mongo_client():
    """
    Connects to the MongoDB client and returns the client object.
    """
    client = MongoClient("mongodb://localhost:27017/")  # MongoDB URL
    return client


def get_bus_details_collection():
    client = get_mongo_client()
    db = client["chatbot_db"]  # Replace with your actual MongoDB database name
    collection = db["bus_details"]
    return collection
