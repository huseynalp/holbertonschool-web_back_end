#!/usr/bin/env python3
"""10-update_topics.py: Update topics of a school document in MongoDB"""

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        name (str): The school name to update.
        topics (list of str): The list of topics to set.

    Returns:
        None
    """
    mongo_collection.update_one(
        {'name': name},          # Filter document by school name
        {'$set': {'topics': topics}}  # Update the 'topics' field
    )
