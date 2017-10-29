#!/bin/env python

#    A-John-Shots - Python module/library for saving Security Hash Algorithms into JSON format.
#    Copyright (C) 2017  Funilrys - Nissar Chababy <contact at funilrys dot com>
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.

#    Original Version: https://github.com/funilrys/A-John-Shots


import hashlib
from os import path


class Hash(object):
    """
    Get and return the hash a file with the given algorithm.

    :param path: A string, the path to the file we have to hash.
    :param algorithm: A string, the algorithm to use.
    :param only_hash: A bool, Return only the desired algorithm if algorithm != 'all'.
    """

    def __init__(self, path, algorithm='sha512', only_hash=False):
        self.VALID_ALGORITHMS = ['all', 'md5',
                                 'sha1', 'sha224', 'sha384', 'sha512']

        self.path = path
        self.algorithm = algorithm
        self.only_hash = only_hash

    def hash_data(self, algo):
        """Get the hash of the given file

        :param algo: A string, the algorithm to use.
        """

        hash_data = getattr(hashlib, algo)()

        with open(self.path, 'rb') as file:
            content = file.read()

            hash_data.update(content)
        return hash_data.hexdigest()

    def get(self):
        """
        Return the hash of the given file
        """

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

        if self.algorithm != 'all' and self.only_hash:
            return result[self.algorithm]
        return result
