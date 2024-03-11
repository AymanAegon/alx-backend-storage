#!/usr/bin/env python3
"""9. Insert a document in Python"""

def insert_school(mongo_collection, **kwargs):
    """Insert a document in Python"""
    obj = {}
    for key, value in kwargs.items():
        obj[key] = value
    result = mongo_collection.insert_many(obj).inserted_id
    return result
