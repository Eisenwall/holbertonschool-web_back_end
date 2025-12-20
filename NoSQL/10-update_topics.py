#!/usr/bin/env python3
"""
10-update_topics.py
Module that updates all topics of a school document based on the name
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name

    Args:
        mongo_collection (pymongo.collection.Collection): Collection object
        name (str): Name of the school to update
        topics (list of str): List of topics to set

    Returns:
        dict: Result of the update operation
    """
    if mongo_collection is None or name is None or topics is None:
        return None
    result = mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
    return result.raw_result
