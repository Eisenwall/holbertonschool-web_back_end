#!/usr/bin/env python3
"""
9-insert_school.py
Module that inserts a new document in a MongoDB collection
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection

    Args:
        mongo_collection (pymongo.collection.Collection): Collection object
        **kwargs: Fields and values to insert

    Returns:
        ObjectId: The _id of the inserted document
    """
    if mongo_collection is None or not kwargs:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
