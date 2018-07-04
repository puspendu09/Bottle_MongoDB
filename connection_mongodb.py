from pymongo import MongoClient


collection = MongoClient('localhost', 27017).students.grades

item = collection.find({})
for doc in item:
    print(doc)
