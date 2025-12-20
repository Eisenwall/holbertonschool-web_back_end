#!/usr/bin/env python3
"""
11-schools_by_topic.py
Module that returns a list of schools having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns all schools that have a specific topic

    Args:
        mongo_collection (pymongo.collection.Collection): Collection object
        topic (str): Topic to search for

    Returns:
        list: List of documents (schools) that have the topic
    """
    if mongo_collection is None or topic is None:
        return []
    return list(mongo_collection.find({ "topics": topic }))
