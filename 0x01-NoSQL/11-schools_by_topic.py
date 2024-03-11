#!/usr/bin/env python3
"""11. Where can I learn Python?"""

def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    arr = []
    for school in list(mongo_collection.find()):
        print(school)
        if topic in school['topics']:
            arr.append(school)
    return arr
