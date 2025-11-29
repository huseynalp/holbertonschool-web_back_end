#!/usr/bin/env python3
"""8-all.py: List all documents in a collection"""

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.

    Returns:
        list: A list of documents (dictionaries) in the collection.
              Returns an empty list if no documents are found.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
