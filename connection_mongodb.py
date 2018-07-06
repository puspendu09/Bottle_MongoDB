from pymongo import MongoClient
from bson.son import SON


db = MongoClient('localhost', 27017).m101

db.inventory.insert_many([
    {"item": "journal",
     "instock": [
         SON([("warehouse", "A"), ("qty", 5)]),
         SON([("warehouse", "C"), ("qty", 15)])]},
    {"item": "notebook",
     "instock": [
         SON([("warehouse", "C"), ("qty", 5)])]},
    {"item": "paper",
     "instock": [
         SON([("warehouse", "A"), ("qty", 60)]),
         SON([("warehouse", "B"), ("qty", 15)])]},
    {"item": "planner",
     "instock": [
         SON([("warehouse", "A"), ("qty", 40)]),
         SON([("warehouse", "B"), ("qty", 5)])]},
    {"item": "postcard",
     "instock": [
         SON([("warehouse", "B"), ("qty", 15)]),
         SON([("warehouse", "C"), ("qty", 35)])]}])
