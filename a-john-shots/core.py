#!/bin/env python


class Core(object):
    """A simple script to get Security Hash Algorithms into JSON format"""

    def __init__(self, path, algorithm='sha512'):
        self.path = path
        self.algorithm = algorithm
