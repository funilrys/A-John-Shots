#!/bin/env python
from os import path
import hashlib


class Hash(object):
    """Return the hash of given file path with a given algorithm

    :param path: A string, the path to the file we have to hash.
    :param algorithm: A string, the algorithm to use.
    """

    def __init__(self, path, algorithm='sha512'):
        self.path = path
        self.algorithm = algorithm

        self.valid_algorithms = ['md5', 'sha1', 'sha224', 'sha384', 'sha512']

    def hash_data(self, algo):
        """Give/get the hash of the given file

        :param algo: A string, the algorithm to use.
        """

        hash_data = getattr(hashlib, algo)()

        with open(self.path, 'rb') as file:
            content = file.read()

            hash_data.update(content)
        return hash_data.hexdigest()

    def get(self):
        """Return the hash of the given file"""

        result = {}
        if path.isfile(self.path) and self.algorithm in self.valid_algorithms:
            result[self.algorithm] = self.hash_data(self.algorithm)
            return result[self.algorithm]
        return None
