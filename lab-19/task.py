"""
Title: NoSQL Blog

Task: Create the db to store your blog posts using Mongo.

In this task you need:
+ create the db, collection and documents
+ insert objects
+ retrieve all objects and object via filtering
+ update at least 1 object
+ delete at least 1 object
"""
import datetime
from typing import Union

from pymongo import MongoClient
from pymongo.collection import Collection

import data


def create_db(client: MongoClient):
    blog_db = client['blog']
    blog_db["user"].insert_many(data.users_data)
    blog_db["post"].insert_many(data.posts_data)


def get_collection(client: MongoClient, db_name: str, collection_name: str, to_print: bool = True):
    blog_db = client[db_name]
    collection = blog_db[collection_name]
    if to_print:
        print('Displaying collection:')
        for document in collection.find():
            print(document)

    return collection


def searcher(collection: Collection, field: str, filter_: Union[str, dict]):
    print('Searching documents:')
    for document in collection.find({field: filter_}):
        print(document)

    return collection.find({field: filter_})


def updater(collection: Collection, filter_: dict, update: dict):
    print('Updating documents..')
    collection.update_many(filter_, update)
    print('Documents are updated.')


def deleter(collection: Collection, filter_: dict):
    print('Deleting documents..')
    collection.delete_many(filter_)
    print('Documents are deleted.')


if __name__ == '__main__':
    with MongoClient(host='localhost', port=27017) as mongo_client:
        create_db(mongo_client)
        post_collection = get_collection(mongo_client, 'blog', 'post', to_print=False)
        searcher(post_collection, 'like_counter', {'$gt': 15})
        updater(post_collection, {'like_counter': {'$gt': 15}}, {'$set': {'like_counter': 15}})
        deleter(post_collection, {'date': {'$eq': datetime.datetime(2023, 1, 3)}})
