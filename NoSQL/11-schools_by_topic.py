#!/usr/bin/env python3
"""
Module for finding schools by topic in a MongoDB collection
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    
    Args:
        mongo_collection: pymongo collection object
        topic: topic searched
        
    Returns:
        List of school documents that contain the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
