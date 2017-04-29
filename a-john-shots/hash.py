#!/bin/env python


class Hash(object):
    """Return the hash of given file path with a given algorithm"""

    def __init__(self, path, algorithm):
        self.path = path
        self.algorithm = algorithm
