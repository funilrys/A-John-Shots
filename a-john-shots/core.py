#!/bin/env python
from hash import Hash
from helpers import unset_empty
from json import dumps
from os import path


class Core(object):
    """A simple script to get Security Hash Algorithms into JSON format

    :param path: A string, the path of the file or the directory we have to return.
    :param algorithm: A string, the algorithm to use when hashing.
    """

    def __init__(self, path, algorithm='sha512'):
        self.path = path
        self.algorithm = algorithm

    def hierarchy(self, hash_of_file):
        """Build the dictionary of data

        :param hash_of_file: A dict, Hash of the current file.
        """

        result = {}
        local_result = result

        hierarchy = unset_empty(self.path.split('/'))
        for funilrys in hierarchy:
            if funilrys == hierarchy[-1]:
                local_result = local_result.setdefault(funilrys, hash_of_file)
            else:
                local_result = local_result.setdefault(funilrys, {})

        return result

    def get(self):
        """Brain of the program"""

        result = {}
        file_hash = {}

        if path.isfile(self.path):
            file_hash = Hash(self.path, self.algorithm, False).get()
            result = self.hierarchy(file_hash)

        return dumps(result, indent=4)
