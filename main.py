from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import List


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def get_database_collection(database: Database, collection_name: str) -> Collection:
    collection = database[collection_name]
    return collection


if __name__ == "__main__":
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "mongo_two"
    collection_name = "employees"

    client = MongoClient(mongodb_host, mongodb_port)
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    collection = get_database_collection(db, collection_name)

    # query = {"age": {"$gt": 40, "$lt": 55}, "name": "Edward"}
    age = [40, 45, 49]
    query = {"age": {"$in": age}}

    # response = collection.find({"age": 39, "name": "Jeremy"}, {"salary": 1, "_id": 0})
    response = collection.find(query, {"_id": 0})
    for i in response:
        print(i)
