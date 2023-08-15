#!/usr/bin/env python3
"""MongoDB Operations with python using pymongo """


def insert_school(mongo_collection, **kwargs):
    """ inserts ne documents in collection """
    return db.mongo_collection.insert(kwargs)