#!/usr/bin/env python3
"""
10-update_topics.py
Module that updates the topics of a school document
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name

    Args:
        mongo_collection (pymongo.collection.Collection): Collection object
        name (str): Name of the school to update
        topics (list): List of topics to set

    Returns:
        None
    """
    if mongo_collection is None or not name or not isinstance(topics, list):
        return
    mongo_collection.update_one(
        { "name": name },
        { "$set": { "topics": topics } }
    )
