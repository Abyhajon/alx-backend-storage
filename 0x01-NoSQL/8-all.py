#!/usr/bin/env python3
""" MongoDB Operations with python """

def list_all(mongo_collection):
    documents = db.mongo_collection.find()
    if documents.count() == 0:
        return []
    return documents