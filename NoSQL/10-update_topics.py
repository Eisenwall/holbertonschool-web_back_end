#!/usr/bin/env python3
""" main_4.py — test update_topics """

from pymongo import MongoClient
update_topics = __import__('10-update_topics').update_topics

def get_ordered_doc(doc):
    """Return a dict with keys in the order _id, name, topics"""
    return {
        "_id": doc.get("_id"),
        "name": doc.get("name"),
        "topics": doc.get("topics")
    }

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    doc_id = school_collection.insert_one({"name": "match_name"}).inserted_id
    new_topics = ["new topic 0", "new topic 1"]
    update_topics(school_collection, "match_name", new_topics)
    doc = school_collection.find_one({"_id": doc_id})
    if get_ordered_doc(doc) == {"_id": doc_id, "name": "match_name", "topics": new_topics}:
        print("OK")
    else:
        print("No the same list of topics:", doc, "/", {"_id": doc_id, "name": "match_name", "topics": new_topics})
    school_collection.delete_one({"_id": doc_id})
