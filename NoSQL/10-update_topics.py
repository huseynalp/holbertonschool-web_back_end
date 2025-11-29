#!/usr/bin/env python3
"""10-update_topics.py: Update topics of a school document based on the name"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of a school document identified by its name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        name (str): The name of the school to update.
        topics (list of str): The new list of topics for the school.

    Returns:
        None
    """
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
