#!/bin/env python3

"""
A John Shots - A tool to get the Security Hash Algorightms (SHA) of all file in a given path.

This submodule provide the hashing logic.

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Contributors:
    Let's contribute to A John Shots!

Project link:
    https://github.com/funilrys/A-John-Shots

License:
::

    MIT License

    Copyright (c) 2017-2019 Nissar Chababy

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
import hashlib
from os import path


class Hash:
    """
    Get and return the hash a file with the given algorithm.

    :param file_path: The absolute path to the file we are working with.
    :type file_path: str

    :param algorithm: The algorithm to use.
    :type algorithm: str

    :param only_hash:
        If :code:`True` return only the desired algorithm
        if algorithm != :code:`all`
    """

    def __init__(self, file_path, algorithm="sha512", only_hash=False):
        self.valid_algorithms = ["all", "md5", "sha1", "sha224", "sha384", "sha512"]

        self.path = file_path
        self.algorithm = algorithm
        self.only_hash = only_hash

    def hash_data(self, algo):
        """
        Get the hash of the globally given file path.

        :param algo: The algorithm to use.
        :type algo: str

        :return: The algo representation of the given file path.
        :rtype: str
        """

        hash_data = getattr(hashlib, algo)()

        with open(self.path, "rb") as file:
            content = file.read()

            hash_data.update(content)
        return hash_data.hexdigest()

    def get(self):
        """
        Return the hash of the given file
        """

        result = {}

        if path.isfile(self.path) and self.algorithm in self.valid_algorithms:
            if self.algorithm == "all":
                del self.valid_algorithms[0]

                for algo in self.valid_algorithms:
                    result[algo] = None
                    result[algo] = self.hash_data(algo)
            else:
                result[self.algorithm] = None
                result[self.algorithm] = self.hash_data(self.algorithm)

        if self.algorithm != "all" and self.only_hash:
            return result[self.algorithm]
        return result
