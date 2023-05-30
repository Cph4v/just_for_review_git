import string
from pymongo import MongoClient
import os
import sys
import json
import pandas as pd
from bson import json_util
import pydantic


# my_mongo = 'mongodb+srv://fr514kh:895022096@cluster0.brg7sma.mongodb.net/?retryWrites=true&w=majority'

# client = MongoClient(my_mongo)

# db = client["sample_analytics"]
# collection = db["accounts"]

# if os.path.isdir("data_json") == False:
#     os.mkdir('./data_json')

# json_data_list = collection.find().limit(10)


# documents = [doc for doc in json_data_list]



# with open("data_json/output.json", "w") as file:
#     json.dump(documents, file, default=json_util.default)
# # for index in documents:
    
# print(list(documents[0].keys()))


class User(pydantic.BaseModel) -> None:
    account_id: int
    limit: str
    products: list[str]

    @pydantic.validator("limit")
    @classmethod
    def limit_validator(cls, value):
        if any(p in value for p in string.punctuation):
            raise ValueError("limit argument mustnt include pinctuations")
        else:
            return value
            

    @pydantic.validator("products")
    @classmethod
    def product_validator(cls, value):
        for product in value:
            if any(p in product for p in string.digits):
                raise ValueError("products argument must not include punctuations")
            else:
                return value



# data = pd.read_json("data_json/output.json")
json_data = [User(**U) for U in json.load(open("data_json/output.json"))]
print(json_data)
# data['products'][0] = 'hert333'
# data['products'][0][0] = 'gerytou555'
# print(data[0:1])
# user1 = User()

# with open("data_json/data.json", mode="w+") as json_file: 
#     for j in collection.find().limit(10):

        # json_file.write(formatted, "a+")


# doc1 = {"_id":7, "shelf":90, "book":"Dune", "author":["hebert ziman", "franckr shore"]}

# doc2 = {"_id":8, "shelf": 98, "book": "harry", 
#         "author": ["hebert sorry", "franckr shorry"]
#         }
# collection.insert_one(doc1)
# collection.insert_many([doc1,doc2])

# results = collection.find({"_id": 8})
# collection.update_many({"shelf": {"$gte": 80}}, {"$set":{"shelf": 696969, "book": "claimed"}})
# collection.update_one({"_id": 8}, {"$set":{"shelf": 98000, "book": "hands on"}})
# print(results)
# results = collection.find({})
# for x in results:
#     print(x)


# for db_name in client.list_database_names():
#     print(db_name)

# db.collection.insertOne()
# db.collection.insertMany([
#     {
#         'tittle': 'hghhghghh',
#         'hghhgh': ['kqqfuqih','jjjjj','dhfWEFU']
#     },
#     {
#         'pittle': 'hguhghghh',
#         'lghhgh': 'kq;fuqih'
#     },
#     {
#         'oitfle': 'hgnhghghh',
#         'hghggf': 'kqmmfuqih'
#     },
# ])
# {"common_name": "Morning Dove","scientific_name": "Zenaida macroura","wingspan_cm": 37.23,"habitat": ["urban areas", "farms", "grassland"],"diet": ["seeds"],}