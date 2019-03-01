#!/bin/env python3

"""
A John Shots - A tool to get the Security Hash Algorightms (SHA) of all file in a given path.

This submodule provide the brain of the module.

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
# pylint: disable=bad-continuation

from os import path
from os import sep as directory_separator
from os import walk

from a_john_shots.defaults import DEFAULT_EXCLUDE
from a_john_shots.hash import Hash
from a_john_shots.helpers import Regex, combine_dicts


class Core:
    """
    The real brain of the module.

    :param file_or_dir_path: The file or directory we are working with.
    :type file_or_dir_path: str

    :param algorithm:
        The SHA to use. Can be one of the following:
        ::

            - all
            - sha1
            - sha224
            - sha384
            - sha51
    :type algorithm: str

    :param search:
        The pattern the filename have to match in order to be
        taken in consideration.
    :type search: str

    :param exclude:
        The pattern the filename have to match in order to be
        excluded.
    :type exclude: str
    """

    def __init__(self, file_or_dir_path, search=None, algorithm="sha512", exclude=None):
        if isinstance(search, str):
            self.search = search
        else:
            self.search = None

        if exclude is None:
            self.exclude = []
        elif isinstance(exclude, list):
            self.exclude = exclude
        else:
            self.exclude = [exclude]

        if file_or_dir_path == ".":
            self.path = f"{file_or_dir_path}{directory_separator}"
        else:
            self.path = file_or_dir_path

        self.algorithm = algorithm
        self.ppath = [self.path]
        self.exclude.extend(DEFAULT_EXCLUDE)

    def get(self):
        """
        Return the :code:`dict` tree representing the given path childs.
        """

        result = {}
        file_hash = {}

        if path.isfile(self.path):
            file_hash = Hash(self.path, self.algorithm, False).get()
            result = self.hierarchy(file_hash)
        elif path.isdir(self.path):
            for root, _, files in walk(self.path):
                for file in files:
                    sub = self.get_childs(root, file)
                    if not self.search:
                        result = combine_dicts(sub, result)
                    elif Regex(file, self.search).match():
                        result = combine_dicts(sub, result)
        else:
            raise Exception("Given file/dir path not found.")

        return result

    def hierarchy(self, hash_of_file):
        """
        Build the hierarchy tree.

        :param hash_of_file: A dict representing a file and its hash.
        :type hash_of_file: dict

        :return: The hierarchy tree.
        :rtype: dict
        """

        result = {}

        for item in self.ppath:
            hierarchy = [x for x in item.split(directory_separator) if x]
            local_result = result

            for funilrys in hierarchy:
                if funilrys == hierarchy[-1]:
                    local_result = local_result.setdefault(funilrys, hash_of_file)
                else:
                    local_result = local_result.setdefault(funilrys, {})

        return result

    def get_childs(self, root, file):
        """
        Get the childs of the current directory.

        :param root: The current root absolute path.
        :type root: str

        :param file: The current file absolute path.
        :type file: str

        :return: A :code:`dict` with the hash of the currently read file.
        :rtype: dict
        """

        result = {}
        path_to_file = f"{root}{directory_separator}{file}"

        if not Regex(path_to_file, self.exclude, return_data=False).loop_matching():
            self.ppath = [x for x in path_to_file.split(self.path) if x]

            file_hash = Hash(path_to_file, self.algorithm).get()
            result = self.hierarchy(file_hash)

        return result
