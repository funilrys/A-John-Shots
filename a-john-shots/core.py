#!/bin/env python
from hash import Hash
from helpers import unset_empty, combine_dicts
from json import dumps
from os import path, walk


class Core(object):
    """A simple script to get Security Hash Algorithms into JSON format

    :param path: A string, the path of the file or the directory we have to return.
    :param algorithm: A string, the algorithm to use when hashing.
    """

    def __init__(self, path, algorithm='sha512'):
        self.DIRECTORY_SEPARATOR = '/'

        self.path = path
        self.ppath = [self.path]
        self.algorithm = algorithm

    def hierarchy(self, hash_of_file):
        """Build the dictionary of data

        :param hash_of_file: A dict, Hash of the current file.
        """

        result = {}

        for item in self.ppath:
            hierarchy = unset_empty(item.split(self.DIRECTORY_SEPARATOR))
            local_result = result

            for funilrys in hierarchy:
                if funilrys == hierarchy[-1]:
                    local_result = local_result.setdefault(
                        funilrys, hash_of_file)
                else:
                    local_result = local_result.setdefault(funilrys, {})

        return result

    def get_file_under_directory(self, root, file):
        """Get the file(s) which is/are under the current directory

        :param root: A string, the current root
        :param file: A string, the current file
        """

        result = {}
        path_to_file = path.join(root, file)
        self.ppath = unset_empty(path_to_file.split(self.path))
        file_hash = Hash(path_to_file, self.algorithm).get()
        result = self.hierarchy(file_hash)

        return result

    def get(self):
        """Brain of the program. In charge to print the results into JSON format"""

        result = {}
        file_hash = {}

        if path.isfile(self.path):
            file_hash = Hash(self.path, self.algorithm, False).get()
            result = self.hierarchy(file_hash, True)
        elif path.isdir(self.path):
            for root, dirs, files in walk(self.path):
                for file in files:
                    sub = self.get_file_under_directory(root, file)
                    result = combine_dicts(sub, result)
        else:
            return None

        return dumps(result, indent=4)
