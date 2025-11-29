#!/usr/bin/env python3
"""9-insert_school.py: Insert a new document into a MongoDB collection"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection using keyword arguments.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        **kwargs: Arbitrary keyword arguments representing the document fields.

    Returns:
        ObjectId: The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
