#!/usr/bin/env python3
"""
10-update_topics.py
Module that updates the topics of a school document
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name
    """
    if mongo_collection is None or not name or not isinstance(topics, list):
        return
    # Update only the topics field without touching other fields
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
