#!/bin/env python

#    A-John-Shots - Python module/library for saving Security Hash Algorithms into JSON format.
#    Copyright (C) 2017  Funilrys - Nissar Chababy <contact at funilrys dot com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#    Original Version: https://github.com/funilrys/A-John-Shots


from os import path
import hashlib


class Hash(object):
    """Return the hash of given file path with a given algorithm

    :param path: A string, the path to the file we have to hash.
    :param algorithm: A string, the algorithm to use.
    """

    def __init__(self, path, algorithm='sha512', only_hash=False):
        self.VALID_ALGORITHMS = ['all', 'md5',
                                 'sha1', 'sha224', 'sha384', 'sha512']

        self.path = path
        self.algorithm = algorithm
        self.only_hash = only_hash

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

        if path.isfile(self.path) and self.algorithm in self.VALID_ALGORITHMS:
            if self.algorithm == 'all':
                del self.VALID_ALGORITHMS[0]
                for algo in self.VALID_ALGORITHMS:
                    result[algo] = None
                    result[algo] = self.hash_data(algo)
            else:
                result[self.algorithm] = None
                result[self.algorithm] = self.hash_data(self.algorithm)

        if self.only_hash:
            return result[self.algorithm]
        return result
