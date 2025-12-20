#!/usr/bin/env python3
"""
8-all.py
Module that lists all documents in a MongoDB collection
"""

def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
        mongo_collection (pymongo.collection.Collection): Collection object

    Returns:
        list: List of documents, empty list if none
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
