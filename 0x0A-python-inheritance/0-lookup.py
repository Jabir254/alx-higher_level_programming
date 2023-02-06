#!/usr/bin/python3

"""Defines an object attribute lookup function."""

def lookup(obj):
    """Returns list of objects available attributes."""
    return (dir(obj))
