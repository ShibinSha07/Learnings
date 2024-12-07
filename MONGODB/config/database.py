from pymongo import MongoClient

client=MongoClient("mongodb+srv://tcr21cs003:1234@cluster0.7yqfh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client.todo_db

collection_name=db["todo_collection"]